#! python3
#loader.py
#
import os
import csv
from datetime import datetime
import categorizer

class record (object):
    '''This class handles each individual item in the budget.'''
    def __init__(self, date, description, withdrawl, deposit, account, category='', tag='', split=''):
        
        #gives values to withdrawl and deposit if NULL.
        if not withdrawl:
            withdrawl = '0'
        if not deposit:
            deposit = '0'
        
        self.date = datetime.strptime(date, '%m/%d/%Y').date()
        self.description = description
        self.withdrawl = float(withdrawl) #convert, saved as strings.
        self.deposit = float(deposit)
        self.account = account
        self.category = category
        self.tag = tag
        self.split = split
        
    def recordValues (self):
        return ('{:%m/%d/%Y}'.format(self.date), 
                           self.description, 
                           self.withdrawl,
                           self.deposit,  
                           self.account, 
                           self.category,
                           self.tag,
                           self.split)
                           
    def similarValues (self):
        return ('{:%m/%d/%Y}'.format(self.date), 
                           self.description, 
                           self.withdrawl,
                           self.deposit,  
                           self.account)

    def __str__(self):
        return ('Date: {:%A, %b %d, %Y}\n'
                'Description: {}\n'
                'Withdrawl: ${}\n'
                'Deposit: ${}\n'
                'Account: {}\n'
                'Category: {}\n'
                'Tag: {}\n'
                'Split Status: {}\n\n'.format(self.date, self.description, self.withdrawl, self.deposit, self.account, self.category, self.tag, self.split))
    
def new_file_list ():
    ''' returns tuple of file .csv names in .//newdata directory '''
    return tuple('.//newdata//{}'.format(file) for file in os.listdir('.//newdata') if file.endswith(".csv"))
  
def create_master_records (fileName):
    """
        Create previously categorized records from raw files.
        
        Parameter: .csv file name of categorized records.
        
        Return: a list of record objects.
    """
    with open (fileName, newline='') as f:
        # createn tuple where each entry represents a record            
        rawData = tuple(row for row in csv.reader(f))
    #rows represent: date, description, withdrawl, deposit, account, category, 
    #tag, and split.
    return [record(row[0],row[1],row[2],row[3], row[4], row[5], row[6], row[7]) for row in rawData]

def create_new_records (fileName):
    """
       Create new records from raw files.
        
       Parameter: .csv file name of new records.
        
       Return: a list of record objects.
    """
    #read raw data from .csv file
    with open (fileName, newline='') as f:            
        rawData = tuple(row for row in csv.reader(f))
    #Check to see what account tag the new data has in it's name.
    if fileName.startswith('.//newdata//credit'):
        account = 'credit'
    elif fileName.startswith('.//newdata//savings'):
        account = 'savings'
    elif fileName.startswith('.//newdata//debit'):
        account = 'debit'
    else:
        print(fileName)
        account = 'no account'
    #rows represent: date, description, withdrawl, deposit, account.
    return [record(row[0],row[1],row[2],row[3], account) for row in rawData]    
    
def load_new_records ():
    records = []
    for file in new_file_list():
        records.extend(create_new_records(file))
    return records
    
def archive_records ():
    for file in os.listdir('.//newdata'):
        if file.endswith(".csv"):
            #os.replace will write over any file with the same name.
            os.replace(".//newdata//{}".format(file), ".//archive//{}".format(file))
    
def delete_duplicates(records):
    uniqueRecords = set()
    newRecords = []
    for record in records:
        if record.recordValues() in uniqueRecords:
            continue
        uniqueRecords.add(record.recordValues())
        newRecords.append(record)
    return newRecords
    
def save_similar_records(records, fileName):
    """
        Save records that are almost duplicates for manual review.
        
        Parameters:
            records(list): list of record objects.
            fileName(str): file to save the similar records to.
            
        Returns:
            the number of similar records found.
    """
    similarRecords = set()
    newRecords = []
    #
    for record in records:
        #if record exists in the set, add to list of similar records.
        if record.similarValues() in similarRecords:
            newRecords.append(record)
            continue
        #if record is unique, add to similarRecords set.
        similarRecords.add(record.similarValues())
    #save similar records to file.
    save_records(newRecords, fileName)
    return len(newRecords)

def save_records (records, fileName):  
    '''Writes records to output.csv file'''
    with open(fileName, 'w', newline='') as f:
        file = csv.writer(f)
        for record in records:
            file.writerow(record.recordValues())
                               
def main ():
    """
        Main function of the loader module. 
        
        Calls:
            load_new_records(): load new transaction records.
            .categorize_records(): classify records into budget
                            categories.
            .save_categories(): save categorization data to categories.py.
            archive_records(): archive new input transaction files.
            create_master_records(): load previously categorized records.
            delete_duplicates(): delete any duplicate records.
            save_similar_records(): save records that are very similar for 
                            later manual review.
            save_records(): save all records to master.csv file.
    """
    print('Loading new records...')
    records = load_new_records()         
    print('loaded')        
    
    newCategories = categorizer.categorizer(records)
    newCategories.categorize_records()
    
    print('\nSaving categories...')    
    newCategories.save_categories()
    print('Saved')
    
    print('archiving records')
    archive_records()
    
    #print('loading master records...')
    #records.extend(create_master_records('master.csv'))
    print('deleting duplicate records')
    records = delete_duplicates(records)
    
    print('Saving similar records for review...')
    similar = save_similar_records(records, 'similar.csv')   
    print('***** {} possible duplicate records to review *****'.format(similar))
    
    print('\nSaving records...')
    save_records(records, 'master2.csv')
    print('Records saved in master2.csv')
        
if __name__=='__main__': 
    main()