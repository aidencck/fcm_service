#!/bin/bash

# 设置颜色变量
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
CYAN='\033[0;36m'
MAGENTA='\033[0;35m'
NC='\033[0m' # No Color

# 打印分隔线
print_separator() {
    local color=$1
    local length=$2
    local char=$3
    printf "${color}%${length}s${NC}\n" | tr " " "$char"
}

# 打印标题
print_title() {
    local title=$1
    local color=$2
    local length=60
    local padding=$(( (length - ${#title} - 2) / 2 ))
    printf "${color}%${padding}s %s %${padding}s${NC}\n" "" "$title" ""
}

# 打印检查项
print_check_item() {
    local status=$1
    local message=$2
    local padding=50
    printf "  %-${padding}s [%s]\n" "$message" "$status"
}

# 进度条显示
show_progress() {
    local current=$1
    local total=$2
    local width=50
    local progress=$((current * width / total))
    local percent=$((current * 100 / total))
    
    printf "\r${CYAN}["
    for ((i=0; i<width; i++)); do
        if [ $i -lt $progress ]; then
            printf "="
        else
            printf " "
        fi
    done
    printf "] %d%%${NC}" $percent
}

# 错误原因收集
declare -a error_reasons

# 添加错误原因
add_error_reason() {
    error_reasons+=("$1")
}

# 显示错误原因
show_error_reasons() {
    if [ ${#error_reasons[@]} -gt 0 ]; then
        print_title "错误原因分析" "$RED"
        for reason in "${error_reasons[@]}"; do
            echo -e "  ${RED}•${NC} $reason"
        done
        echo ""
    fi
}

# 检查命令是否存在
check_command() {
    local cmd=$1
    local required_version=$2
    local current_version=$3
    
    print_title "检查 $cmd 安装" "$BLUE"
    if ! command -v $cmd &> /dev/null; then
        print_check_item "${RED}✗" "$cmd 未安装"
        add_error_reason "$cmd 未安装，请安装 $cmd 并确保其在 PATH 中"
        return 1
    fi
    
    if [ -n "$required_version" ]; then
        if [ "$(printf '%s\n' "$required_version" "$current_version" | sort -V | head -n1)" != "$required_version" ]; then
            print_check_item "${RED}✗" "$cmd 版本过低 (需要 >= $required_version, 当前: $current_version)"
            add_error_reason "$cmd 版本过低，当前版本: $current_version，需要 >= $required_version"
            return 1
        fi
        print_check_item "${GREEN}✓" "$cmd 版本: $current_version"
    else
        print_check_item "${GREEN}✓" "$cmd 已安装"
    fi
    return 0
}

# 检查 Node.js 版本
check_node_version() {
    local required_version="16.0.0"
    local current_version=$(node -v | sed 's/v//')
    check_command "Node.js" "$required_version" "$current_version"
}

# 检查 pnpm 版本
check_pnpm_version() {
    local required_version="7.0.0"
    local current_version=$(pnpm -v)
    check_command "pnpm" "$required_version" "$current_version"
}

# 检查环境变量
check_env_vars() {
    local env_file=".env"
    print_title "检查环境变量配置" "$BLUE"
    
    if [ ! -f "$env_file" ]; then
        print_check_item "${RED}✗" ".env 文件不存在"
        add_error_reason ".env 文件不存在，请创建 .env 文件并配置必要的环境变量"
        return 1
    fi
    
    local required_vars=(
        "VITE_API_BASE_URL"
        "VITE_FIREBASE_API_KEY"
        "VITE_FIREBASE_AUTH_DOMAIN"
        "VITE_FIREBASE_PROJECT_ID"
    )
    
    local all_vars_present=true
    for var in "${required_vars[@]}"; do
        if ! grep -q "^$var=" "$env_file"; then
            print_check_item "${RED}✗" "环境变量 $var 未设置"
            add_error_reason "环境变量 $var 未在 .env 文件中设置"
            all_vars_present=false
        else
            local value=$(grep "^$var=" "$env_file" | cut -d'=' -f2)
            if [ -z "$value" ]; then
                print_check_item "${RED}✗" "环境变量 $var 值为空"
                add_error_reason "环境变量 $var 已设置但值为空"
                all_vars_present=false
            else
                print_check_item "${GREEN}✓" "环境变量 $var 已设置"
            fi
        fi
    done
    
    return $all_vars_present
}

# 检查依赖安装
check_dependencies() {
    print_title "检查项目依赖" "$BLUE"
    
    if [ ! -d "node_modules" ]; then
        print_check_item "${YELLOW}⚠" "node_modules 目录不存在，正在安装依赖..."
        pnpm install
        if [ $? -ne 0 ]; then
            print_check_item "${RED}✗" "依赖安装失败"
            add_error_reason "依赖安装失败，请检查网络连接和 package.json 文件"
            return 1
        fi
        print_check_item "${GREEN}✓" "依赖安装成功"
    else
        print_check_item "${GREEN}✓" "node_modules 目录存在"
        
        local missing_deps=$(pnpm ls --depth=0 | grep -E "✗|ERR!" | wc -l)
        if [ "$missing_deps" -gt 0 ]; then
            print_check_item "${YELLOW}⚠" "发现未安装的依赖，正在安装..."
            pnpm install
            if [ $? -ne 0 ]; then
                print_check_item "${RED}✗" "依赖安装失败"
                add_error_reason "依赖安装失败，请检查网络连接和 package.json 文件"
                return 1
            fi
            print_check_item "${GREEN}✓" "依赖安装成功"
        else
            print_check_item "${GREEN}✓" "所有依赖已正确安装"
        fi
    fi
    return 0
}

# 检查项目结构
check_project_structure() {
    print_title "检查项目结构" "$BLUE"
    
    local required_dirs=("src" "public")
    local required_files=("package.json" "vite.config.ts" "tsconfig.json")
    
    for dir in "${required_dirs[@]}"; do
        if [ ! -d "$dir" ]; then
            print_check_item "${RED}✗" "目录 $dir 不存在"
            add_error_reason "项目目录 $dir 不存在，请确保项目结构完整"
            return 1
        else
            print_check_item "${GREEN}✓" "目录 $dir 存在"
        fi
    done
    
    for file in "${required_files[@]}"; do
        if [ ! -f "$file" ]; then
            print_check_item "${RED}✗" "文件 $file 不存在"
            add_error_reason "配置文件 $file 不存在，请确保项目配置完整"
            return 1
        else
            print_check_item "${GREEN}✓" "文件 $file 存在"
        fi
    done
    
    return 0
}

# 执行环境检查
perform_environment_check() {
    print_separator "$MAGENTA" 60 "="
    print_title "开始环境检查" "$YELLOW"
    print_separator "$MAGENTA" 60 "="
    echo ""
    
    local total_checks=6
    local current_check=0
    
    local checks=(
        "check_node_version"
        "check_pnpm_version"
        "check_env_vars"
        "check_dependencies"
        "check_project_structure"
    )
    
    local all_checks_passed=true
    
    for check in "${checks[@]}"; do
        current_check=$((current_check + 1))
        show_progress $current_check $total_checks
        echo ""
        
        if ! $check; then
            all_checks_passed=false
        fi
        echo ""
    done
    
    show_progress $total_checks $total_checks
    echo ""
    print_separator "$MAGENTA" 60 "="
    
    if [ "$all_checks_passed" = false ]; then
        print_title "环境检查未通过" "$RED"
        show_error_reasons
        print_separator "$MAGENTA" 60 "="
        
        # 添加跳过选项
        while true; do
            read -p "是否继续运行？(y/n): " choice
            case $choice in
                [Yy]* )
                    print_title "跳过环境检查继续运行" "$YELLOW"
                    print_separator "$MAGENTA" 60 "="
                    echo ""
                    return 0
                    ;;
                [Nn]* )
                    print_title "退出程序" "$RED"
                    print_separator "$MAGENTA" 60 "="
                    exit 1
                    ;;
                * )
                    echo "请输入 y 或 n"
                    ;;
            esac
        done
    fi
    
    print_title "所有环境检查通过" "$GREEN"
    print_separator "$MAGENTA" 60 "="
    echo ""
}

# 显示环境信息
show_env_info() {
    print_separator "$MAGENTA" 60 "="
    print_title "项目环境信息" "$YELLOW"
    print_separator "$MAGENTA" 60 "="
    
    local info_items=(
        "项目名称: My App"
        "版本: 0.0.1"
        "Node.js 版本: $(node -v)"
        "pnpm 版本: $(pnpm -v)"
        "API 基础地址: http://localhost:3000"
        "Firebase 配置: 已启用"
        "日志功能: 已启用"
        "分析功能: 已禁用"
    )
    
    for item in "${info_items[@]}"; do
        printf "${BLUE}%-20s${NC} %s\n" "${item%%:*}" "${item#*:}"
    done
    
    print_separator "$MAGENTA" 60 "="
    echo ""
}

# 显示菜单
show_menu() {
    print_title "Frontend Project Runner" "$BLUE"
    echo "请选择要执行的操作："
    echo "1) 开发环境运行"
    echo "2) 生产环境构建"
    echo "3) 预览生产构建"
    echo "4) 运行测试"
    echo "5) 运行测试（监视模式）"
    echo "6) 运行测试（UI模式）"
    echo "7) 运行测试覆盖率报告"
    echo "8) 代码格式化和 lint"
    echo "0) 退出"
    print_separator "$MAGENTA" 60 "-"
}

# 执行选择的命令
execute_choice() {
    case $1 in
        1)
            print_title "启动开发服务器" "$GREEN"
            pnpm dev
            ;;
        2)
            print_title "构建生产版本" "$GREEN"
            pnpm build
            ;;
        3)
            print_title "预览生产构建" "$GREEN"
            pnpm preview
            ;;
        4)
            print_title "运行测试" "$GREEN"
            pnpm test
            ;;
        5)
            print_title "运行测试（监视模式）" "$GREEN"
            pnpm test:watch
            ;;
        6)
            print_title "运行测试（UI模式）" "$GREEN"
            pnpm test:ui
            ;;
        7)
            print_title "运行测试覆盖率报告" "$GREEN"
            pnpm test:coverage
            ;;
        8)
            print_title "运行代码格式化和 lint" "$GREEN"
            pnpm format && pnpm lint
            ;;
        0)
            print_title "退出程序" "$YELLOW"
            exit 0
            ;;
        *)
            print_title "无效的选择" "$RED"
            ;;
    esac
}

# 主程序
perform_environment_check
while true; do
    show_env_info
    show_menu
    read -p "请输入选项 (0-8): " choice
    echo ""
    execute_choice $choice
    echo ""
done 