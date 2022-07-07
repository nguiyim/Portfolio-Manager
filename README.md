# Portfolio-Manager
Learning labs curated by BBIT

0-SECURITIES
Problem Definition
We want to create a class that can be used to represent a security. Securities have names which are unique identifiers of what they represent. Additionally securities have a monetary value associated with them but for now we'll ignore any valuations. The class we create should satisfy the following.

Allow for the name of a security to be stored on object construction & via a setter function
Allow for the name of the security to be retrieved via a getter

1-POSITIONS
Problem Definition
We want to build a class that represents a position. We should be able to construct a position with a security object we created, as well as a seed or initial position. We may also want to create a position without constructing a security object by using the security name we'd like our position to represent.

We'd expect the ability to get the security object the position represents along with the current position value. Lastly we'd want to be able to update the position value with the ability to add to the existing position & set the position value. If a position seed or update results in a short position we'd expect an error to be thrown.

Allow for a position to be created with a security name or object and a seed position value
Allow for gathering of the position's security and position value
Allow for updating of the position's size via addition & setting

2-ACCOUNT
