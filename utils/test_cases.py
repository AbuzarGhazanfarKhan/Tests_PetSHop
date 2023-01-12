def test_cases(number):
    return testCases[number]


testCases = [
    ['TEST_01_HomePage_TEST#01', 'when user goes to home page, page should be loaded'],#..0
    ['TEST_02_HomePage_TEST#02', 'In Home page, when user search "Tiger" , User should see result for "Tiger Shark" '],#..1
    ['TEST_03_HomePage_TEST#03', 'In Home page, when user click on any category , User should be navigated to Categorys page '],#..2
    ['TEST_04_HomePage_TEST#04', 'In Home page, when user click on "Cart" Icon , User should be navigated to Shopping Cart page '],#..3
    ['TEST_05_HomePage_TEST#04', 'In Home page, when user click "Sing in" button, he should see Sign in Page'],#.4
    ['TEST_06_LogIn_TEST#01', 'In Login Page, On submitting empty form , User will should get a message "please enter your username and password" '],#..5
    ['TEST_07_LogIn_TEST#02', 'In Login Page, when user login with a valid user, he should see Home Page'],#..6
    ['TEST_09_LogIn_TEST#03', 'In Login Page, when user login with a in-valid user, he should see Error Message'],#..7
    ['TEST_10_LogIn_TEST#04', 'In Login page, when user click "Register" button, he should see Sign up Page'],#..8
    ['TEST_11_LogIn_TEST#01', 'In SignUp page, when user Submit Empty Form He/She should see a Validation'],#..9
    ['TEST_12_LogIn_TEST#02', 'In SignUp page, when user Submit Empty Form He/She should see a Validation'],#..10
    ['TEST_13_LogIn_TEST#03', 'In SignUp page, when user Submit Empty Form He/She should see a Validation'],#..11
    ['TEST_14_LogIn_TEST#04', 'In SignUp page, when user Submit Empty Form He/She should see a Validation'],#..12
    ['TEST_15_LogIn_TEST#05', 'In SignUp page, when user Submit Empty Form He/She should see a Validation'],#..13
    ['TEST_16_LogIn_TEST#06', 'In SignUp page, when user Submit Empty Form He/She should see a Validation'],#..14
    ['TEST_17_LogIn_TEST#07', 'In SignUp page, when user Submit Empty Form He/She should see a Validation'],#..15
    ['TEST_18_Cart_TEST#01', 'On HomePage, Clicking on Cart Icon should load Up cart Page and Cart Table'],#..16
    ['TEST_19_Cart_TEST#02', 'In Shopping Cart Page, If there is nothing added in the cart, Sub Total should be $0.00'],#..17
    ['TEST_20_Cart_TEST#03', 'In Shopping Cart Page, After adding product to cart should calculate subtotal as per the amount of product'],#..18
    ['TEST_21_Cart_TEST#04', 'In Shopping Cart Page, After removing all product subtotal should be $0.00 and cart should be empty'],#..19
    ['TEST_22_Cart_TEST#05', 'In Shopping Cart Page, Proceed to checkout should navigate to loggin page if not loggedin'],#..20
    ['TEST_23_Cart_TEST#06', 'In Shopping Cart Page, Proceed to checkout should navigate to loggin page if not loggedin and after logging in should be redirected to order confirmation'],#..21
    ['TEST_24_Cart_TEST#07', 'Logged in user should smoothly add product to cart , proceed to check out and recieve order receipt'],#..22
    ['TEST_19_Cart_TEST#02', 'In Shopping Cart Page, Cart Should be empty for first User'],#..23
    ['TEST_24_Update_Acoount_Info_TEST#07', 'Logged in user should smoothly add product to update_Acoount_Info , proceed to check out and recieve order receipt'],#..24
    ['TEST_24_Update_Acoount_Info_TEST#07', 'Logged in user should smoothly add product to cart , proceed to check out and recieve order receipt'],#..25
]
