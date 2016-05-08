# Instrukcja do zajęć labolatoryjnych WZPI 8.05.2016

## Interakcja z cloud9
1. Utwórz konto na [cloud9](https://c9.io). Możesz użyć swojego konta na githubie do autoryzacji.
2. W zakładce *Workspaces* wybierz opcję *Create a new workspace*
3. Wpisz dowolną nazwę, w polu *Clone from git* wpisz `novirael/qapp-ansible` a jako template wybierz *Python*. Potwierdź.
4. Po uruchomieniu środowiska wpisz w konsoli następujące komendy

  ```
  sudo pip install -r requirements.txt
  sudo pip install setuptools --upgrade
  ```

## Konfiguracja aplikacji webowej QApp
1. Zobacz jakie pliki zostały przez nas przygotowane.
2. Uruchom komendę konfigurująca aplikację webową - `./qapp.py setup`.
3. Zobacz jakie zmiany zostały wprowadzone.
2. Uruchom komendę aktualizującą aplikację webową - `./qapp.py update`.
3. Zobacz jakie zmiany zostały wprowadzone.
4. Poczekaj aż prowadzący dokona zmian w kodzie aplikacji a następnie uruchom ponownie - `./qapp.py update`
5. Zobacz jakie zmiany zostały wprowadzone.

## Zmiany w konfiguracji
1. Utwórz task który utworzy pusty katalog z logami - *logs* w katalogu projektu *code/qapp/*.
2. Utwórz task który wykona następującą komendę podczas update `./manage.py collectstatic`
3. Utwórz task który wykona backup bazy danych przed wykonaniem update.

### Linki
1. [Dokumentacja Ansible](http://docs.ansible.com/ansible)