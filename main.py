from scrape_modes import Mode

def save_to_file(content):
    with open('problems.txt', 'a') as f:
        for data in content:
            f.write(f"{data}\n")
        f.close()



home_page = 'https://www.codingame.com/training'
link = input("Clash URL: ")

m = Mode(link)
m.bypass_welcome()
m.which_mode()
save_to_file(m.get_code())


