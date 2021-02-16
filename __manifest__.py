{
	'name': 'LiquorStore Management Application',
	'description': 'Manage mixes of all types of alcohol and buy',
	'author': 'Miguel Roman , Juan Vicenta Esparza , Fredy Romero',
	'depends': ['base'],
	'application': True,
	'data': [
		'views/liquorstore_menu.xml',
		'views/alcohol_view.xml',
		'security/liquorstore_security.xml',
		'security/ir.model.access.csv',
		'views/alcohol_tipos_view.xml',
	],
	'demo': [
		'data/liquorstore_demo.xml',
		'data/liquorstore_tipos_demo.xml'

	],
}
