
state_to_find = "Ohio"

with open('DATA/presidents.txt') as pres_in:
    with open('potus.txt', 'a') as pres_out:
        for raw_line in pres_in:
            term, last_name, first_name, dob, dod, bplace, bstate, *_ = raw_line.split(':')
            if bstate == state_to_find:
                record = f"{first_name}\t{last_name}\t{bplace}\n"
                pres_out.write(record)


