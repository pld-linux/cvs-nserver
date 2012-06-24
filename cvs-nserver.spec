Summary:	Concurrent Versions System
Summary(de):    Concurrent-Versioning-System
Summary(fr):    Un syst�me pour maintenir � jour des fichiers
Summary(pl):    Concurrent Versioning System
Summary(tr):    S�r�m denetim sistemi
Name:		cvs-nserver
Version:	1.10.8.4
Release:	1
License:	GPL
Group:		Development/Version Control
Group(pl):	Programowanie/Zarz�dzanie wersjami
Source0:	http://alexm.here.ru/cvs-nserver/download/%{name}-%{version}.tar.gz
Patch0:		cvs-nserver-PAM_fix.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CVS is a version control system, which allows you to keep old versions
of files (usually source code), keep a log of who, when, and why
changes occurred, etc., like RCS or SCCS. Unlike the simpler systems,
CVS does not just operate on one file at a time or one directory at a
time, but operates on hierarchical collections of directories
consisting of version controlled files. CVS helps to manage releases
and to control the concurrent editing of source files among multiple
authors. CVS allows triggers to enable/log/control various operations
and works well over a wide area network.

%description -l de
CVS ist ein Frontend f�r das RCS(1)-Revisionskontrollsystem, das den
Begriff der Revisionskontrolle von einer Sammlung von Dateien in einem
einzelnen Verzeichnis auf eine ganze Hierarchie ausweitet, bestehend
aus revisionskontrollierten Dateien. Diese Verzeichnisse und Dateien
lassen sich zu einer Software-Release kombinieren. CVS bietet die
Funktionen, die zur Verwaltung von Software-Releases und zur
�berwachung der gleichzeitigen Bearbeitung von Quelldateien durch
mehrere Software- Entwickler notwendig sind.

%description -l fr
"CVS" signifie "Concurrent Version System". C'est un syst�me de
comparaison de versions de fichiers, qui peut garder une trace des
changements apport�s � des fichiers (le plus souvent, les fichiers des
sources d'un programme). CVS conserve seulement les diff�rences, et
non l'int�gralit� d'un fichier r�cent et d'un fichier plus ancien. A
chaque modification d'un fichier, CVS garde (entre autres) le nom de
la personne ayant fait la modification, la raison justifiant cette
modification, et la date � laquelle celle-ci a eu lieu. CVS est tr�s
utile pour g�rer la mise en commun des modifications apport�es par
plusieurs personnes travaillant en parall�le sur les m�mes fichiers.
Au lieu de garder plusieurs versions des fichiers dans un seul
r�pertoire, CVS cr�e une s�rie de r�pertoires, chacun contenant une
nouvelle version des fichiers. Ces r�pertoires et ces fichiers peuvent
ensuite �tre regroup�s pour former la version la plus � jour du
logiciel. Installez ce package si vous avez besoin d'utiliser un
syst�me de contr�le de version.

%description -l pl
CVS jest nak�adk� na rcs (Revision Control System, czyli w wolnym
t�umaczeniu system kontroli wersji zasob�w), kt�ry rozszerza
mo�liwo�ci rcs'a z narz�dzia do kontroli zbioru plik�w w pojedynczym
katalogu o mo�liwo�� kontroli zbioru hierarchicznie u�o�onych katalog�w
z plikami. Z pomoc� CVS w �atwy spos�b mo�na zarz�dza� kodem �r�d�owym
opracowywanym przez nawet bardzo du�e zesp�y programist�w
umo�liwiaj�c �ledzenie i kontrol� wszystkich zmian w trakcie pracy nad
projektami i wypuszczaniem pe�nych wersji oprogramowania (release).

%description -l tr
CVS (Concurrent Versioning System), tek bir dizindeki dosya
toplulu�unun s�r�m denetimini, denetimi yap�lm�� dizinlerin hiyerar�ik
toplulu�una geni�leten rcs(1) s�r�m denetim sisteminin �n y�z�d�r. Bu
dizin ve dosyalar, bir yaz�l�m yay�n� olu�turma amac�yla biraraya
getirilebilir. CVS, bu yaz�l�m yay�nlar�n�n y�netilmesini ve kaynak
dosyalar� bak�m�n�n birden �ok yaz�l�m geli�tiricisi taraf�ndan
e�zamanl� olarak yap�lmas�n� kontrol etmek i�in gereken i�levleri
sa�lar.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%configure \
	--enable-pam
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} installdirs
%{__make} PAMDIR=$RPM_BUILD_ROOT/etc/pam.d install
%{__make} install-setuid
rm -f $RPM_BUILD_ROOT%{_prefix}/info/cvs*
%{__make} install-info

gzip -9nf $RPM_BUILD_ROOT{%{_infodir}/*,%{_mandir}/man?/*} \
	BUGS FAQ HACKING MINOR-BUGS NEWS PROJECTS README TESTS TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/cvs
%attr(755,root,root) %{_bindir}/cvschkpw
%attr(755,root,root) %{_bindir}/cvspasswd
%attr(755,root,root) %{_bindir}/cvs-pserver
%attr(755,root,root) %{_bindir}/cvs-nserver
%attr(755,root,root) %{_bindir}/checkpassword
%attr(755,root,root) %{_bindir}/checkpassword-pam
%attr(755,root,root) %{_bindir}/cvsbug
%attr(755,root,root) %{_bindir}/rcs2log
/etc/pam.d/cvspserver
%{_mandir}/man1/cvs.1*
%{_mandir}/man5/cvs.5*
%{_mandir}/man8/cvsbug.8*
%{_mandir}/man8/cvs-nserver.8*
%{_mandir}/man8/cvs-pserver.8*
%{_mandir}/man8/cvs-server.8*
%{_infodir}/cvs*
%{_libdir}/cvs
