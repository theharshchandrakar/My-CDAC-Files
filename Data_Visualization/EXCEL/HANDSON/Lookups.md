**LOOKUPS**
we created joins using lookups

Transaction and Location
=VLOOKUP(C2,Location!$B$3:$E$159,2,False)
=VLOOKUP(C2,Location!$B$3:$E$159,3,False)

Transactions and Product
=HLOOKUP(B2,Product!$C$5:$O$8,2,FALSE)