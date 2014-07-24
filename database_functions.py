def insertUnit(session, targetUnit):
    table = targetUnit.sql_getTable()

    json = targetUnit.reprJSON()
    values = json.keys()

    columns = [val for val in values]
    columns = str(columns).strip('[]').replace("\'", "")

    valueSubs = ['%(' + val + ')s' for val in values]

    valueSubsString = str(valueSubs).strip('[]').replace("\'", "")

    _query = " INSERT INTO " + table + " ( " + columns + " ) \
  VALUES ( " + valueSubsString + ") "

    session.execute(_query, json)


def resetDB(session, schemaDataFile):
    # session.execute( cqlCommands)
    line_number = 0
    with open('./data.cql', encoding='utf-8') as schemaDataFile:
        for command in schemaDataFile:
            # print('{:>4} {}'.format(line_number, command.rstrip()))
            session.execute(command.strip())
            # line_number += 1


def queryAll(session, targetUnit):
    table = targetUnit.sql_getTable()
    _query = "SELECT * FROM " + table

    user_rows = session.execute(_query)
    for row in user_rows:
        print("Row: ", row)
