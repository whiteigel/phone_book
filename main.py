from app.logic import read_csv, pretty_contacts, phone_num_converter, \
  duplicates_processing, removing_empty_strings, write_csv

if __name__ == '__main__':
    pretty_contacts = pretty_contacts(read_csv('phonebook_raw.csv'))
    updated_phone_numbers = phone_num_converter(pretty_contacts)
    no_dups_contacts = duplicates_processing(updated_phone_numbers)
    to_write = removing_empty_strings(no_dups_contacts)
    write_csv(to_write)
