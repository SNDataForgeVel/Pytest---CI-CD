from pyspark.sql.functions import col

def FilterRows(df,columnName,value,operator):
    operatorMap = {
            "==": col(columnName) == value,
            "!=": col(columnName) != value,
            ">":  col(columnName) > value,
            ">=": col(columnName) >= value,
            "<":  col(columnName) < value,
            "<=": col(columnName) <= value,
    }
    return df.filter(~operatorMap[operator]) 


def FilterIsNullRows(df,columnName):
    return df.filter(df.filter(columnName).isNull()) 