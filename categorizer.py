#! python3
#categorizer.py

"""
    Module consists of a categorizer class that categorizes new transaction 
    records.  Each record has a shortened record_tag created from the 
    transaction description.  This is used to categorize the item into one
    of several budget categories, and also categorizes whether the transaction
    is to be split or not.  
    
    Tags, categories, and split statuses are saved to categories.py as dicts.
    If the tag has not been previously seen, the object asks the user to 
    classify the record.
"""

import re
import pprint
#import previous information for regex search, categories, and split status.
import categories as c

class categorizer(object):
    """
        Categorize a list of transactions into budget categories and set
        whether or not to split the item.  
        
        Parameter:
            records(list): list of record objects that represent transactions.
            
        Attributes:
            categories(dict): dict representing category:list(tags) pairs.
            split(dict): dict representing split:list(tags) pairs.
            regexPattern(string): joined values of regexPattern list into a 
                                  single string seperated by pipe character.
                                  Used to search for tags with regex.
            
        Calls:
            create_record_tags(): creates a short tag for each record.
    """
    
    def __init__(self, records):
        self.records = records
        self.categories = c.categories
        self.split = c.split
        self.regexPattern = '|'.join(c.regexPattern)
        self.create_record_tags()

    def create_record_tags (self):
        """
            Create short identifying tags from record description using 
            the regexPattern string.
        """
        regex = re.compile('{}'.format(self.regexPattern))
        for record in self.records:
            try:
                record.tag = regex.search(record.description).group()
            except:
                record.tag = record.description
            
    def save_categories(self):
        """
           Save the regexPattern string as a list, categories as a dict, and
           split as a dict to categories.py for later use.
        """
        with open('categories.py', 'w') as f:
            f.write("'''Contains dicts for categorization of tags'''\n\n")
            f.write('regexPattern = {}\n\n'.format(pprint.pformat(self.regexPattern.split('|'))))
            f.write('categories = {}\n\n'.format(pprint.pformat(self.categories)))
            f.write('split = {}\n'.format(pprint.pformat(self.split)))
        
    def category_of_tag (self, categories, tag):
        """
           Get the category key in categories for a given tag.
           
           Parameters:
               categories(dict): a dict in form 'key':['tags'].
               tag(string): the given tag to search for.
               
            Returns:
                The category that a given tag is in or None.
        """
        for category, values in categories.items():
            if tag in values:
                return category

    def get_category(self, record):
        """
            Get the category of a record.
            
            Returns:
                The category of the record if the tag is known.  Otherwise,
                asks the user to categorize the record and returns the given 
                category.
                
            Calls:
                category_of_tag()
        """
        #Check to see if the record tag has a known category.        
        category = self.category_of_tag(self.categories, record.tag)
        if record.tag == 'CHQ#' and record.withdrawl == 1600:
            record.tag = 'RENT'
            if record.tag not in self.categories['Rent']:
                self.categories.setdefault('Rent', []).append(record.tag)
            return 'Rent'
        elif record.tag == 'PAYMENT - THANK YOU' and record.account == 'credit':
            if record.tag not in self.categories['Transfer']:            
                self.categories.setdefault('Transfer', []).append(record.tag)            
            return 'Transfer'
        elif category:
            return category
        elif record.deposit:
            self.categories.setdefault('Deposit', []).append(record.tag)
            return 'Deposit'
        elif any(x in record.tag for x in ['TFR-TO','TFR-FR']):
            record.tag = 'TRANSFER'
            if record.tag not in self.categories['Transfer']:
                self.categories.setdefault('Transfer', []).append(record.tag)
            return 'Transfer'
        
        #Record tag unknown, therefore ask user how to categorize the record.
        print('\nDescription: {}'.format(record.description))
        print('Withdrawl: {}'.format(record.withdrawl))
        print('Date: {:%A, %b %d, %Y}'.format(record.date))
        newCategory = input("What category to put '{}' in?\n".format(record.tag)).capitalize()            
        if newCategory not in self.categories:
            print('Creating new category...')
        #Creates a new category if it doesn't exist, or adds to a known cat.
        self.categories.setdefault(newCategory, []).append(record.tag)
        return newCategory
        
    def _set_ask_split(self, record):
        """
            Called when a record is categorized as 'ask' in split.  User asked
            to specify if the record should be split.  Saves response to 
            record.split, but keeps split status as 'ask' for later records
            with the same tag.
            
            Returns:
                'split': if the record is to be split.
                '!split': if the record is to not be split.
        """
        while True:
            print("I am to 'ask' if item should be split") 
            print('Descripition: {}'.format(record.description))
            print('Date: {:%A, %b %d, %Y}'.format(record.date))
            print('Withdraw amount: ${}'.format(record.withdrawl))
            ask = input("Would you like to split {}? Y/N\n".format(record.tag)).upper()
            if ask == 'Y':
                return 'split'
            elif ask == 'N':
                return '!split'
            print('invalid input')
                
    def get_split(self, record):
        """
            Get whether or not the record is to be split.  First see if a 
            record's category has a split status, otherwise create a split
            status at the category level.
            
            If the category split status is 'skip', then see if the record's
            tag has a split status.  If not then create one.
            
            Returns:
                categorySplit: if the record's category has a known split 
                          status that is not 'skip'.
                newCategorySplit: if the record's category had no previous
                          split status, and the status is not 'skip'.
                tagSplit: if the record's tag has a known split status that
                          is not 'ask'.
                newSplit: if the record's tag has no known split.  Ask the 
                          user to provide one and return it if not 'ask'.  
                _set_ask_split(): if the record's tag split status is 'ask'.
                
            Calls:
                category_of_tag()
                _set_ask_split()
        """
        #Check to see if the category has a split status.
        categorySplit = self.category_of_tag(self.split, record.category)
        if categorySplit in ['split', '!split']:
            return categorySplit
        #if category is not in split at all, set category split behaviour.
        elif not categorySplit:
            while True:
                newCategorySplit = input("Would you like to 'split', !split', or 'skip' the category?\n" )
                if newCategorySplit in ['split', '!split']:
                    self.split[newCategorySplit].append(record.category)
                    return newCategorySplit
                elif newCategorySplit == 'skip':
                    self.split[newCategorySplit].append(record.category)
                    break
                print('Invalid input, try again')
        
        #Since category is skip, find if tag is in split and return value.
        tagSplit = self.category_of_tag(self.split, record.tag)
        if tagSplit:
            if tagSplit in ['split', '!split']:
                return tagSplit
            return self._set_ask_split(record)
        #if tag is not in split at all, set new split value.
        while True:
            newSplit = input("Should {} be 'split', '!split', or 'ask'?\n".format(record.tag))
            if newSplit == 'ask':
                self.split[newSplit].append(record.tag)
                return self._set_ask_split(record)
            elif newSplit in ['split', '!split']:
                self.split[newSplit].append(record.tag)
                return newSplit
            print('invalid input')
                
    def categorize_records (self):
        """
            This is the main method of the categorizer object.  Loop through
            all records.  First set the budget category of the records, then
            set the split status of the record.
            
            Calls:
                get_category()
                get_split()
        """
        for record in self.records:
            record.category = self.get_category(record)
            print('\n{} is in category {}'.format(record.tag, record.category))
            
            record.split = self.get_split(record)
            print("{} is set to the '{}' category".format(record.tag, record.split))
                