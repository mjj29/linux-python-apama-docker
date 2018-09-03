from apama.eplplugin import EPLPluginBase, EPLAction


class test(EPLPluginBase):
	def __init__(self, init):
		super(test, self).__init__(init)

	@EPLAction('action<>')
	def helloWorld(self):
		self.getLogger().info("Hello World")

