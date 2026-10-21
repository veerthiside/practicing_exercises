with open("Basics\\Exercise\\13_read_write_files\\stocks.csv", "r", encoding="utf-8") as infile, open("Basics\\Exercise\\13_read_write_files\\q2_first_try_output.csv", "w", encoding="utf-8") as op_file:
    infile.readline() # why? - so the for loop starts from 2nd line
    op_file.write("Company Name,PE Ratio,PB Ratio\n")
    for line in infile:
        parts = line.strip().split(',') # first splits at , then strip the starting and ending whiteline
        # print(parts)

        company_name = parts[0]
        price = float(parts[1])
        earnings_per_share = float(parts[2])
        book_value = float(parts[3])
        
        # print(company_name)
        # print(price)
        # print(earnings_per_share)
        # print(book_value)
        
        # print(company_name)
        pe_ratio = round(price/earnings_per_share, 2)
        price_to_book_ratio = round(price/book_value, 2)
        # print(pe_ratio)
        # print(price_to_book_ratio)
        op_file.write(f"{company_name},{pe_ratio},{price_to_book_ratio}\n") 


    
    
        



