Co potrzeba do odpalenia?
	-python 2.7
		-bottle framework // pip install bottle
		-pymongo // pip install pymongo
	
	-MongoDb 3.0.1
	-VirtualBox SDK // w folderze Vboxa jest folder "/sdk/install", wbijacie do niego i uruchamiacie skrypt 'vboxapisetup.py' (pami�ta� o ustawieniu sciezki instalacji, tak jak w linku na fb, kt�ry pablo wrzuci�)
	
Jak wszystko poinstalowane, to:
	-odpali� server MongoDb (w konsoli wpisa�: mongod)
	-w osobnej konsoli odpali� aplikacje (zvb.py)
	-w przegl�darce wklepa� adres, kt�ry bedzie w konsoli (powinno by� co� takiego http://localhost:8082/)
	
Na razie to co jest dzia�a tylko dla lokalnych maszyn.
Co jest potrzebne do obs�ugi host�w zdalnie trzeba si� dowiedzie� (jaki� WebService? prawdopodobnie to co zosta�o zrobione nie b�dzie potrzebne). 

Ma�o czasu zosta�o na ogarni�cie czegokolwiek!

Co jest co?
zvb.py - g��wny skrypt, nawi�zuje po��czenie z baz� danych, uruchamia aplikacj�, kt�ra czeka na requesty (url)
		 
zvb_vbox.py - skrypt obs�uguj�cy vboxa (uruchamianie maszyn itp)

zvbDAO.py - Data Access Object - skrypt ��cz�cy si� z baz� i wykonuj�cy na niej bezpo�rednio wszystkie operacje

folder 'views' - template'y do stron