Co potrzeba do odpalenia?
	-python 2.7
		-bottle framework // pip install bottle
		-pymongo // pip install pymongo
	
	-MongoDb 3.0.1
	-VirtualBox SDK // w folderze Vboxa jest folder "/sdk/install", wbijacie do niego i uruchamiacie skrypt 'vboxapisetup.py' (pamiêtaæ o ustawieniu sciezki instalacji, tak jak w linku na fb, który pablo wrzuci³)
	
Jak wszystko poinstalowane, to:
	-odpaliæ server MongoDb (w konsoli wpisaæ: mongod)
	-w osobnej konsoli odpaliæ aplikacje (zvb.py)
	-w przegl¹darce wklepaæ adres, który bedzie w konsoli (powinno byæ coœ takiego http://localhost:8082/)
	
Na razie to co jest dzia³a tylko dla lokalnych maszyn.
Co jest potrzebne do obs³ugi hostów zdalnie trzeba siê dowiedzieæ (jakiœ WebService? prawdopodobnie to co zosta³o zrobione nie bêdzie potrzebne). 

Ma³o czasu zosta³o na ogarniêcie czegokolwiek!

Co jest co?
zvb.py - g³ówny skrypt, nawi¹zuje po³¹czenie z baz¹ danych, uruchamia aplikacjê, która czeka na requesty (url)
		 
zvb_vbox.py - skrypt obs³uguj¹cy vboxa (uruchamianie maszyn itp)

zvbDAO.py - Data Access Object - skrypt ³¹cz¹cy siê z baz¹ i wykonuj¹cy na niej bezpoœrednio wszystkie operacje

folder 'views' - template'y do stron