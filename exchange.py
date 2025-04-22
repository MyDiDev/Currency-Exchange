import os, platform

def exchange_money(budget:float, exchange_rate:float) -> float:
    return round(budget / exchange_rate, 2)

def title() -> None:
    print('''\033[36;1m

 ▗▄▄▖▗▖ ▗▖▗▄▄▖ ▗▄▄▖ ▗▄▄▄▖▗▖  ▗▖ ▗▄▄▖▗▖  ▗▖    
▐▌   ▐▌ ▐▌▐▌ ▐▌▐▌ ▐▌▐▌   ▐▛▚▖▐▌▐▌    ▝▚▞▘     
▐▌   ▐▌ ▐▌▐▛▀▚▖▐▛▀▚▖▐▛▀▀▘▐▌ ▝▜▌▐▌     ▐▌      
▝▚▄▄▖▝▚▄▞▘▐▌ ▐▌▐▌ ▐▌▐▙▄▄▖▐▌  ▐▌▝▚▄▄▖  ▐▌      
                                              
                                              
                                              
▗▄▄▄▖▗▖  ▗▖ ▗▄▄▖▗▖ ▗▖ ▗▄▖ ▗▖  ▗▖ ▗▄▄▖▗▄▄▄▖    
▐▌    ▝▚▞▘ ▐▌   ▐▌ ▐▌▐▌ ▐▌▐▛▚▖▐▌▐▌   ▐▌       
▐▛▀▀▘  ▐▌  ▐▌   ▐▛▀▜▌▐▛▀▜▌▐▌ ▝▜▌▐▌▝▜▌▐▛▀▀▘    
▐▙▄▄▖▗▞▘▝▚▖▝▚▄▄▖▐▌ ▐▌▐▌ ▐▌▐▌  ▐▌▝▚▄▞▘▐▙▄▄▖    
                                              
                                              
                                              

\033[0m''')

def main() -> None:
    while True:
        os.system('cls') if platform.system() == "Windows" else os.system('clear')
        
        title()

        try:
            budget_input: str = input("\033[34;1mAmount: \033[0m").strip()
            rate_input: str = input("\033[34;1mRate: \033[0m").strip()
            
            budget: float = float(budget_input.replace(' ', '').replace(',', ''))
            rate: float = float(rate_input.replace(' ', '').replace(',', ''))
            
            result: float = exchange_money(budget, rate)

            print(f"{result:,} $")
            input("\033[33m\nPresiona Enter para Continuar...\n\033[0m")
        except ValueError as e:
            print(f"\033[31m\nIngrese valores validos\033[0m")
            continue
        except KeyboardInterrupt:
            print("\033[33m\n\nSaliendo...\033[0m")
            exit()

if __name__ == '__main__':
    main()
