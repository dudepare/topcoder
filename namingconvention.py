# Top coder problem statement
# https://community.topcoder.com/stat?c=problem_statement&pm=13521&rd=16081
import unittest

class NamingConvention:

	def toCamelCase(self, variableName):

		process = variableName.split('_')
		for i in range(len(process)):
			if i != 0:
				process[i] = process[i].capitalize()
		return ''.join(process)


class TestNamingConvention(unittest.TestCase):

	def setUp(self):
		self.testObj = NamingConvention()

	def callFn(self, parameter):
		return self.testObj.toCamelCase(parameter)

	def testLots(self):
		self.assertEqual("tearHereOnTheLine",
		                 self.callFn("tear_here_on_the_line"))
		self.assertEqual("tOPCODER", self.callFn("t_o_p_c_o_d_e_r"))
		self.assertEqual("aBCDEFGHIJKLMNOPQRSsssssss",
		                 self.callFn("a_b_c_d_e_f_g_h_i_j_k_l_m_n_o_p_q_r_ssssssss"))
		self.assertEqual("aBCDEFGHIJKLMNOPQRSTUVWXYz",
		                 self.callFn("a_b_c_d_e_f_g_h_i_j_k_l_m_n_o_p_q_r_s_t_u_v_w_x_yz"))


	def testOne(self):
		self.assertEqual("variable", self.callFn("variable"))
		self.assertEqual("a", self.callFn("a"))
		self.assertEqual("abbbbbbjsjabbbbbbjsjabbbbbbjsjabbbbbbjs",
		                 self.callFn("abbbbbbjsjabbbbbbjsjabbbbbbjsjabbbbbbjs"))

	def testTwo(self):
		self.assertEqual("aBbbbbbb", self.callFn("a_bbbbbbb"))
		self.assertEqual("aaaaaaaB", self.callFn("aaaaaaa_b"))


if __name__ == '__main__':
	unittest.main()
