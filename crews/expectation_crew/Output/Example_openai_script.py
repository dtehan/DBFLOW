# This script build the great expectations config for the DT310750.
###########################################################################################
# Great Expectations environment creation script
#
# Required packagages: python 3.11, teradataml, crewai, crewai-tools, great_expectations
#
#
###########################################################################################

###############################################
# Begining of configuration of Data Context

import great_expectations as gx

#create the context
data_context = gx.get_context(mode="file")

#add the data source to the context
data_source_name = ""
database_name = ""
connection_string = ""
data_source = data_context.data_sources.add_or_update_sql(data_source_name, connection_string=connection_string)

###############################################
# Checkpoints - actions

action_list = [
    # This Action updates the Data Docs static website with the Validation
    #   Results after the Checkpoint is run.
    gx.checkpoint.UpdateDataDocsAction(
        name="update_all_data_docs",
    ),
]

result_format={"result_format": "COMPLETE"}

###############################################
# Building data assets, expectations, validations

# dynamic code block
table_name = "housing_train_binary"

# static code block
table_asset = data_context.data_sources.get(data_source_name).add_table_asset(table_name=table_name, name=table_name, schema_name=database_name)
batch = data_context.data_sources.get(data_source_name).get_asset(table_name).add_batch_definition_whole_table(name=table_name)
data_context.suites.add(gx.ExpectationSuite(name=table_name))

# dynamic code block
data_context.suites.get(table_name).add_expectation(gx.expectations.ExpectColumnValuesToBeUnique(column="sn"))
data_context.suites.get(table_name).add_expectation(gx.expectations.ExpectColumnValuesToNotBeNull(column="sn"))
data_context.suites.get(table_name).add_expectation(gx.expectations.ExpectColumnValuesToNotBeNull(column="price"))
data_context.suites.get(table_name).add_expectation(gx.expectations.ExpectColumnValuesToNotBeNull(column="lotsize"))
data_context.suites.get(table_name).add_expectation(gx.expectations.ExpectColumnValuesToNotBeNull(column="bedrooms"))
data_context.suites.get(table_name).add_expectation(gx.expectations.ExpectColumnValuesToNotBeNull(column="bathrms"))
data_context.suites.get(table_name).add_expectation(gx.expectations.ExpectColumnValuesToNotBeNull(column="stories"))
data_context.suites.get(table_name).add_expectation(gx.expectations.ExpectColumnValueLengthsToBeBetween(column="driveway", max_value=10))
data_context.suites.get(table_name).add_expectation(gx.expectations.ExpectColumnValueLengthsToBeBetween(column="recroom", max_value=10))
data_context.suites.get(table_name).add_expectation(gx.expectations.ExpectColumnValueLengthsToBeBetween(column="fullbase", max_value=10))
data_context.suites.get(table_name).add_expectation(gx.expectations.ExpectColumnValueLengthsToBeBetween(column="gashw", max_value=10))
data_context.suites.get(table_name).add_expectation(gx.expectations.ExpectColumnValueLengthsToBeBetween(column="airco", max_value=10))
data_context.suites.get(table_name).add_expectation(gx.expectations.ExpectColumnValuesToNotBeNull(column="garagepl"))
data_context.suites.get(table_name).add_expectation(gx.expectations.ExpectColumnValueLengthsToBeBetween(column="prefarea", max_value=10))
data_context.suites.get(table_name).add_expectation(gx.expectations.ExpectColumnValueLengthsToBeBetween(column="homestyle", max_value=20))

# static code block
data_context.suites.get(table_name).save()
data_context.validation_definitions.add(gx.ValidationDefinition(name=table_name, data=batch, suite=data_context.suites.get(table_name)))
data_context.checkpoints.add(gx.Checkpoint(name=table_name, validation_definitions=[data_context.validation_definitions.get(table_name)], actions=action_list, result_format=result_format))
checkpoint = data_context.checkpoints.get(table_name)
checkpoint.run()
checkpoint.save()


# dynamic code block
table_name = "ibm_stock"

# static code block
table_asset = data_context.data_sources.get(data_source_name).add_table_asset(table_name=table_name, name=table_name, schema_name=database_name)
batch = data_context.data_sources.get(data_source_name).get_asset(table_name).add_batch_definition_whole_table(name=table_name)
data_context.suites.add(gx.ExpectationSuite(name=table_name))

# dynamic code block
data_context.suites.get(table_name).add_expectation(gx.expectations.ExpectColumnValuesToBeUnique(column="id"))
data_context.suites.get(table_name).add_expectation(gx.expectations.ExpectColumnValuesToNotBeNull(column="id"))
data_context.suites.get(table_name).add_expectation(gx.expectations.ExpectColumnValueLengthsToBeBetween(column="name", max_value=15))
data_context.suites.get(table_name).add_expectation(gx.expectations.ExpectColumnValuesToNotBeNull(column="name"))
data_context.suites.get(table_name).add_expectation(gx.expectations.ExpectColumnValuesToNotBeNull(column="period"))
data_context.suites.get(table_name).add_expectation(gx.expectations.ExpectColumnValuesToNotBeNull(column="stockprice"))

# static code block
data_context.suites.get(table_name).save()
data_context.validation_definitions.add(gx.ValidationDefinition(name=table_name, data=batch, suite=data_context.suites.get(table_name)))
data_context.checkpoints.add(gx.Checkpoint(name=table_name, validation_definitions=[data_context.validation_definitions.get(table_name)], actions=action_list, result_format=result_format))
checkpoint = data_context.checkpoints.get(table_name)
checkpoint.run()
checkpoint.save()


# dynamic code block
table_name = "mydata"

# static code block
table_asset = data_context.data_sources.get(data_source_name).add_table_asset(table_name=table_name, name=table_name, schema_name=database_name)
batch = data_context.data_sources.get(data_source_name).get_asset(table_name).add_batch_definition_whole_table(name=table_name)
data_context.suites.add(gx.ExpectationSuite(name=table_name))

# dynamic code block
data_context.suites.get(table_name).add_expectation(gx.expectations.ExpectColumnValuesToNotBeNull(column="timestamp"))
data_context.suites.get(table_name).add_expectation(gx.expectations.ExpectColumnValueLengthsToBeBetween(column="timestamp", max_value=1024))
data_context.suites.get(table_name).add_expectation(gx.expectations.ExpectColumnValuesToNotBeNull(column="value"))

# static code block
data_context.suites.get(table_name).save()
data_context.validation_definitions.add(gx.ValidationDefinition(name=table_name, data=batch, suite=data_context.suites.get(table_name)))
data_context.checkpoints.add(gx.Checkpoint(name=table_name, validation_definitions=[data_context.validation_definitions.get(table_name)], actions=action_list, result_format=result_format))
checkpoint = data_context.checkpoints.get(table_name)
checkpoint.run()
checkpoint.save()


# dynamic code block
table_name = "student"

# static code block
table_asset = data_context.data_sources.get(data_source_name).add_table_asset(table_name=table_name, name=table_name, schema_name=database_name)
batch = data_context.data_sources.get(data_source_name).get_asset(table_name).add_batch_definition_whole_table(name=table_name)
data_context.suites.add(gx.ExpectationSuite(name=table_name))

# dynamic code block
data_context.suites.get(table_name).add_expectation(gx.expectations.ExpectColumnValuesToBeUnique(column="Student_ID"))
data_context.suites.get(table_name).add_expectation(gx.expectations.ExpectColumnValuesToNotBeNull(column="Student_ID"))
data_context.suites.get(table_name).add_expectation(gx.expectations.ExpectColumnValuesToNotBeNull(column="Name"))
data_context.suites.get(table_name).add_expectation(gx.expectations.ExpectColumnValueLengthsToBeBetween(column="Name", max_value=1024))
data_context.suites.get(table_name).add_expectation(gx.expectations.ExpectColumnValuesToNotBeNull(column="Course_ID"))
data_context.suites.get(table_name).add_expectation(gx.expectations.ExpectColumnValuesToNotBeNull(column="Marks"))
data_context.suites.get(table_name).add_expectation(gx.expectations.ExpectColumnValuesToBeBetween(column="Marks", min_value=0, max_value=100))

# static code block
data_context.suites.get(table_name).save()
data_context.validation_definitions.add(gx.ValidationDefinition(name=table_name, data=batch, suite=data_context.suites.get(table_name)))
data_context.checkpoints.add(gx.Checkpoint(name=table_name, validation_definitions=[data_context.validation_definitions.get(table_name)], actions=action_list, result_format=result_format))
checkpoint = data_context.checkpoints.get(table_name)
checkpoint.run()
checkpoint.save()

###############################################
# set up the store directory

expectation_store_directory = "my_expectations_store/"
data_context.variables.config.stores["expectations_store"]["store_backend"]["base_directory"] = expectation_store_directory

validation_store_directory = "my_validation_store/"
data_context.variables.config.stores["validation_definition_store"]["store_backend"]["base_directory"] = validation_store_directory

checkpoint_store_directory = "my_checkpoint_store/"
data_context.variables.config.stores["checkpoint_store"]["store_backend"]["base_directory"] = checkpoint_store_directory

validation_results_store_directory = "my_validation_results_store/"
data_context.variables.config.stores["validation_results_store"]["store_backend"]["base_directory"] = validation_results_store_directory

# Define a Data Docs site configuration dictionary
base_directory = "uncommitted/data_docs/local_site/"  # this is the default path (relative to the root folder of the Data Context) but can be changed as required
site_config = {
    "class_name": "SiteBuilder",
    "site_index_builder": {"class_name": "DefaultSiteIndexBuilder"},
    "store_backend": {
        "class_name": "TupleFilesystemStoreBackend",
        "base_directory": base_directory,
    },
}

# Add the Data Docs configuration to the Data Context
site_name = "my_data_docs_site"
data_context.add_data_docs_site(site_name=site_name, site_config=site_config)

# Manually build the Data Docs
data_context.build_data_docs(site_names=site_name)

data_context.open_data_docs()


