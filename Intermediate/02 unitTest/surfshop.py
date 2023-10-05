# Write your code below:
import surfshop
import unittest

class surfShopTests(unittest.TestCase):
  #@classmethod
  def setUp(self):
    self.cart = surfshop.ShoppingCart()

  def test_add_surfboards_1(self):
    message = self.cart.add_surfboards(quantity=1)
    self.assertEqual(message, f'Successfully added 1 surfboard to cart!')

  def test_add_surfboards_multi(self):
    for quantity in range(2,5):
      with self.subTest(quantity):
        message = self.cart.add_surfboards(quantity=quantity)
        self.assertEqual(message, f'Successfully added {quantity} surfboards to cart!')
        self.cart = surfshop.ShoppingCart() #ensure the cart is reset each time to avoid the limit


  '''
  # commented out as it's now refactored for parameterisation
  def test_add_surfboards_2(self):
    message = self.cart.add_surfboards(quantity=2)
    self.assertEqual(message, f'Successfully added 2 surfboards to cart!')'''

  @unittest.skip #skipped as part of project saying that the limit is removed for the off season.
  def test_add_surfboards_5(self):
    self.assertRaises(surfshop.TooManyBoardsError, self.cart.add_surfboards, 5)

  def test_apply_locals_discount(self):
    localTest = self.cart.apply_locals_discount()
    self.assertTrue(self.cart.locals_discount)



    
unittest.main()