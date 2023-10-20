import selfservice

def main():

    tables = selfservice.get_tables()
    selfservice.change_table_owner(tables, "selfservice")

if __name__ == "__main__":
    main()
