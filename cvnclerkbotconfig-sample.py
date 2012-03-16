# Configuration file for clerkbot.py

# Required settings

## IRC nick name, also used to identify with NickServ
nickname = "CVN-ClerkBot"
## NickServ password
password = ""
## IRC real name (appended to this is " {version}")
realname = "Helper bot for the CVN. CVN-ClerkBot "
# IRC server hostname
HOST = "irc.freenode.net"
# IRC server connecting port
PORT = 6667

# Static configuration (used when useMySQL is not True)

## Initial list of channels to join onconnect
channels = ["#cvn-sandbox"]

# MySQL config

## None of the below will be used unless useMySQL is True
useMySQL = False
## MySQL server to connect to
sqlhost = ""
## Port to connect to
sqlport = 3306
## MySQL server username
## This mysql user needs the rights to use SELECT, DELETE, and INSERT statements
sqlname = ""
## Password for the above username
sqlpw = ""
## Name of the database to use
## The database must have at least one table, "channels"
schema = ""