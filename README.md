# MyPkmnTcgPocketList

#### Collection and Wishlist in markdown (.md) format for Pokemon TCG Pocket

#### All game data obtained from https://github.com/flibustier/pokemon-tcg-pocket-database

#### Empy markdown files available in "EmptyLists" folder

#### Code in Python for fetching from repo and generating lists available in "SourceCode" folder

#### If you plan to use this system to track your collection, instructions are below:
- You can copy the entire repo, but update or overwrite the files inside "_MyCards" by copying/pasting the empty ones
- When filled, run the .py file inside "SourceCode" and call the function "genWishlist()" to update your wishlist file at the repo main directory



#### Code explanation
- Some global variables to get urls and filenames are defined at the first lines.
- getCards(getFromUrl=False) function either loads data from the urls or from json files at "SourceCode" folder, returns 3 json lists (cards, sets, rarity).
- setNamesTup() and setNamesDict() are auxiliary functions to associate all IDs and set names, returns tuple list or dict.
- cardsFromSet(setCode) gets all cards of selected set, returns json list.
- saveMarkdown(setCode=None) saves the selected set cards in empty .md files, if selected is None saves all. Saves lines in checklist format "- [ ] Number - Name - Rarity".
- genWishlist(filenameList=glob.glob("..\\_MyCards\\*.md"), outFilename="..\\_Wishlist.md") reads the filled .md files at "_MyCards" folder and writes all non-ticked cards in "_Wishlist.md" at the main directory.


