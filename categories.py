'''Contains dicts for categorization of tags'''

regexPattern = ['PAYMENT.*',
 'CITY OF .*',
 'CANADIAN ACADEMY.*',
 'CANADA WIDE PARKING',
 'NEW YORK FRIES',
 'ESSO',
 'SHELL',
 'THE HOME DEPOT',
 'WAL-MART',
 'BED BATH & BEYOND',
 'THE FRESH TEA SHOP',
 'EA \\*STAR WARS',
 'THE WINE SHOP',
 'WWW.NEWEGG.COM',
 'Amazon.ca',
 '407ETR',
 "MCDONALD'S",
 'COM PHO ASIA',
 'R & P',
 'THE PITA PIT',
 'HK TRAVEL CENTRES',
 'TPA.*',
 'WESTJET',
 'OSLA',
 'AMERICAN ACADEMY OF AUDIO',
 'TFR-TO',
 'TD ATM W/D',
 'CANADA           RIT',
 'SPL             LOAN',
 'OSA              INS',
 'CHQ#',
 'MONTHLY ACCOUNT FEE',
 'ACCT BAL REBATE',
 '\\S+\\s\\S*']

categories = {'Bills': ['NETFLIX.COM ', 'TELUS MOBILITY', 'TELUS MOBLTY'],
 'Business': ['CANADIAN ACADEMY OF AUDIOTORONTO',
              'OSLA',
              'AMERICAN ACADEMY OF AUDIO'],
 'Cash': ['TD ATM W/D', 'NON-TD ATM'],
 'Deposit': ['MOBILE DEPOSIT',
             'CANADA           RIT',
             'GC 3160-DEPOSIT',
             'ACCT BAL REBATE',
             'COIN DEP',
             'GC 2040-DEPOSIT',
             'FRAUD OFFSETTING',
             'IP214 TFR-FR'],
 'Entertainment': ['MEADOWVALE THEATER', 'CINEPLEX 8030', 'FAMOUS PLAYER'],
 'Fast food': ['TIM HORTONS',
               'YUKI SUSHI',
               'RAPIDO BURRITO',
               "MCDONALD'S",
               'TERIYAKI EXP',
               'NEW YORK FRIES',
               'STARBUCKS 04292',
               'QUIZNOS #3527',
               'THE PITA PIT',
               'R & P',
               'HK TRAVEL CENTRES',
               'ONROUTE #01171',
               'THE FRESH TEA SHOP',
               'ALBALISA GOURMET',
               'RED BULB',
               'STARBUCKS #0429'],
 'Fee': ['E-TRANSFER FEE', 'MONTHLY ACCOUNT FEE', 'OTHER BANK'],
 'Fraud': ['EA *STAR WARS'],
 'Gas': ['ESSO', 'SHELL', "WALEE'S ESSO"],
 'Groceries': ['METRO #771',
               'METRO #26',
               'THE WINE SHOP',
               'ZEHRS #54',
               'BULK BARN',
               'LCBO/RAO #0226'],
 'Health': ['LORD DUFFERIN'],
 'Other': ['TICKETKING ROYA'],
 'Payment': ['CHQ#'],
 'Personal': ['SHOPPERSDRUGMART0858 ', 'PARKERS CLEANERS'],
 'Rent': ['RENT'],
 'Restaurants': ['PICKLE BARREL',
                 'COM PHO ASIA',
                 'MILESTONES #5223',
                 'DAIRY QUEEN',
                 'BAGEL WORLD',
                 'SYMPOSIUM CAFE',
                 'CORA BREAKFAST',
                 "JACK ASTOR'S",
                 'MEXICAN FOOD',
                 'FIAZZA FRESH',
                 'BANGKOK THAI',
                 'TOPPERS PIZZA',
                 '3 GUYS',
                 'MI-NE SUSHI',
                 'ORA RESTAURANT',
                 'CORIANDER KITCHEN',
                 'SUSHI DEN'],
 'Shopping': ['Amazon.ca',
              'WAL-MART',
              'PURDYS CHOCOLATIER',
              'CHAPTERS 784',
              'Amazon *Marketplce',
              'BED BATH & BEYOND',
              'SPORT CHEK',
              'PAYPAL *AMMAGRECO',
              'WWW.NEWEGG.COM',
              'CDN TIRE',
              'PANDORA UCM',
              'BEST BUY',
              'THE HOME DEPOT',
              'ALTON GREEN',
              'PAYPAL PTE'],
 'Taxes': ['INTUIT CANADA'],
 'Transfer': ['PAYMENT - THANK YOU', 'TRANSFER'],
 'Transportation': ['MTO RUS-',
                    'CANADA WIDE PARKING',
                    'ORANGEVILLE HYUNDAI',
                    'CITY OF OTTAWA PARKING   OTTAWA',
                    '407ETR',
                    'TPA "CP 171"             TORONTO',
                    'SPL             LOAN',
                    'OSA              INS'],
 'Travel': ['WESTJET'],
 'Utilities': ['TSI INTERNET', 'EMAIL TFR']}

split = {'!split': ['Fast food',
            'Gas',
            'Transportation',
            'Deposit',
            'Taxes',
            'Bills',
            'PURDYS CHOCOLATIER',
            'CHAPTERS 784',
            'SPORT CHEK',
            'Business',
            'WWW.NEWEGG.COM',
            'PANDORA UCM',
            '3 GUYS',
            'Personal',
            'Fraud',
            'Fee',
            'CINEPLEX 8030',
            'FAMOUS PLAYER',
            'Cash',
            'Other',
            'Health',
            'Transfer'],
 'ask': ['PICKLE BARREL',
         'Amazon.ca',
         'WAL-MART',
         'Amazon *Marketplce',
         'BED BATH & BEYOND',
         'MILESTONES #5223',
         'DAIRY QUEEN',
         'BAGEL WORLD',
         'SYMPOSIUM CAFE',
         'CORA BREAKFAST',
         'CDN TIRE',
         "JACK ASTOR'S",
         'BEST BUY',
         'MI-NE SUSHI',
         'ORA RESTAURANT',
         'WESTJET',
         'THE HOME DEPOT',
         'ALTON GREEN',
         'PAYPAL PTE',
         'CHQ#',
         'PAYPAL *AMMAGRECO',
         'MEXICAN FOOD',
         'FIAZZA FRESH',
         'CORIANDER KITCHEN'],
 'skip': ['Restaurants', 'Entertainment', 'Shopping', 'Travel', 'Payment'],
 'split': ['Groceries',
           'Utilities',
           'MEADOWVALE THEATER',
           'COM PHO ASIA',
           'BANGKOK THAI',
           'TOPPERS PIZZA',
           'SUSHI DEN',
           'Rent']}
