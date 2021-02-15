{
	'name': 'LiquorStore Management Application',
	'description': 'Manage mixes of all types of alcohol and buy',
	'author': 'Miguel Roman , Juan Vicenta Esparza , Fredy Romero',
	'depends': ['base'],
	'application': True,
	'data': [
		'views/liquorstore_menu.xml',
		'views/alcohol_view.xml',
		'security/ir.model.access.csv',
		'security/liquorstore_security.xml',
	],
}
