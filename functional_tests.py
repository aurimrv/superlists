from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# Edith ouviu falar de uma nova aplicação online interessante
		# para lista de tarefas. Ela decide verificar a homepage

		self.browser.get("http://localhost:8000")

		# Ela percebe que o título da página e o cabeçalho mencionam
		# listas de tarefas (to-do)

		self.assertIn('To-Do', self.browser.title)
		#header_text = self.browser.find_element_by_tag_name('h1').text
		header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
		self.assertIn('To-Do', header_text)
		
		# Ela é convidada a inserir um item de tarefa imediatamente

		
		inputbox = self.browser.find_element(By.ID, 'id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
		)

		# Ela digita "Buy peacock feathers" (Comprar penas de pavão)
		# em uma nova caixa de texto (o hobby de Edith é fazer iscas
		# para pesca com fly)

		inputbox.send_keys('Buy peacock feathers')


		# Quando ela tecla enter, a página é atualizada, e agora
		# a página lista "1 - Buy peacock feathers" como um item em 
		# uma lista de tarefas

		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)

		table = self.browser.find_element(By.ID,'id_list_table')
		rows = table.find_elements(By.TAG_NAME, 'tr')
		self.assertTrue(
			any(row.text == '1: Buy peacock feathers' for row in rows)
		)

		# Ainda continua havendo uma caixa de texto convidando-a a 
		# acrescentar outro item. Ela insere "Use peacock feathers 
		# make a fly" (Usar penas de pavão para fazer um fly - 
		# Edith é bem metódica)

		self.fail('Finish the test!')

		# A página é atualizada novamente e agora mostra os dois
		# itens em sua lista

		# Edith se pergunta se o site lembrará de sua lista. Então
		# ela nota que o site gerou um URL único para ela -- há um 
		# pequeno texto explicativo para isso.

		# Ela acessa essa URL -- sua lista de tarefas continua lá.

		# Satisfeita, ela volta a dormir

if __name__ == '__main__':
	unittest.main()