# Address Normalization
- Performed Address Normalization on random addresses
- Used python3

# Problem Statement
Normalize unstructured raw Indian addresses by segregating personal information and address to a defined json structure. Addresses can contain spelling mistakes which need to be corrected and addresses need to be geocoded.

# Our Idea
- We fetched the pincode from each line of address.
- Used those pincodes to get to know the City, State, Locality.
- From this info we were able to get the geocodes.
- We performed data sanitization to ensure that no misspelling exists.
- We then finally outputed the collected data in json format. 
- This output was then written to a json file.

# Libraries used
- pgeocode
- json<br>
These can easily be installed using "pip3 install <library-name>"

# How to run this application
- Clone this repository to a code editor
- Either open the file Address-normalization.py and then click on run icon of the code editor
- Or in the terminal write:
    - python Address-normalization.py

# Note
- For the addresses that doesnot include a pincode or for addreses that weren't recognized by our library, our application returned "NaN".

