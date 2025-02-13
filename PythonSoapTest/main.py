# Netcash notification
# Field No:	Field Name:	Alpha / Numeric / Boolean	Description:
# 1	TransactionAccepted	B	“true” means the transaction was successful
# 2	CardHolderIpAddr	AN	This is the original IP the request was made from
# 3	RequestTrace	AN	This is a unique trace id for the transaction. This id can be used to retrieve additional information from the 3rd Party transaction logs
# 4	Reference	AN	The unique reference sent to Netcash in the original request
# 5	Extra1	AN	The extra field sent in the m4 variable when you made the reques
# 6	Extra2	AN	The extra field sent in the m5 variable when you made the request
# 7	Extra3	AN	The extra field sent up in the m6 variable when you made the request
# 8	Amount	N	This is the amount sent Netcash in the original request
# 9	Method	N	1 Credit card
# 2 Bank EFT
# 3 Retail
# 4 Ozow
# 5 MasterPass
# 6 Visa Checkout
# 7 Masterpass QR
# 8 Mobicred
# 9 Payflex
# 10 Flash1Voucher
# The below four (4) fields are only returned if:

# The transaction was a Credit Card payment
# M14 (tokenise card) field is set to True
# “Test Mode” in the NetConnector Profile in the Netcash Account is set to false
# 10	ccToken	AN	Credit Card Vault GUiD
# 11	ccHolder	AN	Credit Cardholder name
# 12	ccMasked	AN	Masked Credit Card number
# 13	ccExpiry	N	Credit Card expiry date MMCCYY
