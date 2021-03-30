from world_sentiment import average_sentiment
from sqlalchemy.orm import sessionmaker
from sqlalchemy import insert
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
import sqlalchemy
from datetime import datetime
from database_con import add_comparison

def main():

    today = datetime.today().strftime("%Y-%m-%d")

    print('What does the world prefer?')
    first = input()
    print('...or...')
    second = input()
    print('\n')

    first_score = average_sentiment(first)
    second_score = average_sentiment(second)

    if first_score > second_score:
        data = (first, second, first)
        print(f'Humans of Twitter prefer {first} over {second}.')

    elif first_score < second_score:
        data = (first, second, second)
        print(f'Humans of Twitter prefer {second} over {first}.')
        
    else:
        data = (first, second, 'Tie')
        print(f"Humans of Twitter don't have preference between {first} and {second}.")

    add_comparison(today, *data)

if __name__ == "__main__":
    main()