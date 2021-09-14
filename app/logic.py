import csv
import re

PHONE_PATTERN_RAW = r'(\+7|8)(\s*)(\(*)(\d{3})(\)*)(\s*)' \
                     r'(\-*)(\d{3})(\s*)(\-*)(\d{2})(\s*)(\-*)' \
                     r'(\d{2})(\s*)(\(*)(доб)*(\.*)(\s*)(\d+)*(\)*)'
PHONE_PATTERN_PRETTY = r'+7(\4)\8-\11-\14\15\17\18\20'


def read_csv(file):
    with open(file) as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
        return contacts_list


def pretty_contacts(list_of_contacts):
    new_contact_list = []
    for ind, elm in enumerate(list_of_contacts):
        lastname = elm[0]
        firstname = elm[1]
        surname = elm[2]
        organization = elm[3]
        position = elm[4]
        phone = elm[5]
        email = elm[6]
        fio = [lastname, firstname, surname]
        fio_joined = ' '.join(fio)
        fio_split = fio_joined.split(' ')
        fio_split = list(filter(None, fio_split))
        if len(fio_split) < 3:
            fio_split.append('')
        lastname = fio_split[0]
        firstname = fio_split[1]
        surname = fio_split[2]
        contact_card = [lastname, firstname, surname, organization, position, phone, email]
        new_contact_list.append(contact_card)
    return new_contact_list


def phone_num_converter(list_of_contacts):
    contacts_list_updated = []
    for card in list_of_contacts:
        card_as_string = ','.join(card)
        card_new_phone = re.sub(PHONE_PATTERN_RAW, PHONE_PATTERN_PRETTY, card_as_string)
        card_as_list = card_new_phone.split(',')
        contacts_list_updated.append(card_as_list)
    del contacts_list_updated[0]
    return contacts_list_updated


def duplicates_processing(list_of_contacts):
    for card in list_of_contacts:
        for card_dup in list_of_contacts:
            if card[0] == card_dup[0] and card[1] == card_dup[1] and card is not card_dup:
                if card[2] == '':
                    card[2] = card_dup[2]
                if card[3] == '':
                    card[3] = card_dup[3]
                if card[4] == '':
                    card[4] = card_dup[4]
                if card[5] == '':
                    card[5] = card_dup[5]
                if card[6] == '':
                    card[6] = card_dup[6]
        refined_list = []
        for card in list_of_contacts:
            if card not in refined_list:
                refined_list.append(card)
    return refined_list


def removing_empty_strings(list_of_contacts):
    contacts_list_cleared = []
    for card in list_of_contacts:
        card = list(filter(None, card))
        contacts_list_cleared.append(card)
    return contacts_list_cleared


def write_csv(list_of_contacts):
    with open("phonebook.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(list_of_contacts)
