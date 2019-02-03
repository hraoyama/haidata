Easy Example
============

Say you had some data processing and cleaning in mind for some columns:

.. code-block:: python
   :linenos:
   
   import pandas as pd
   df = pd.read_csv('myDataSource.csv')
   df['Transaction_ID'] = 'MYDEPARTMENT_' + df['Transaction_ID'].astype(str).fillna('_')
      
And would like to apply this processing to many different data sources and make it available 
as a modular process to your organization's members, including non developers. That is where HaiData comes in:

* Place your data processing in a function that takes two parameters; the input DataFrame and a dictionary that will encapsulate its arguments in key-value pairs. Place the functions in a separate source file in order for it to port easily to other projects and environments.

  .. code-block:: python
     :linenos:
      
      import pandas as pd
      def set_my_department(df, argsDict):
        source_col_name = argsDict.get('source_col', None)
        if source_col_name is not None:
          department_name = argsDict.get('department_name', 'SANITATION')
          df[source_col_name] = department_name + '_' + df[source_col_name].astype(str).fillna('_')


* You now have two options to incorporate your function in the data cleaning process.

  - Manually create a JSON file that does just your processing
  - Programmatically create the same

  Of course it is possible to add your processing to existing configurations:
  



