#
# TODO: build with shared ode, lua
#
Summary:	Clone of across/elma games
Summary(pl):	Klon gry across/elma
Name:		xmoto
Version:	0.1.6
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/xmoto/%{name}-%{version}-src.tar.gz
# Source0-md5:	b5d11e0f90ab5ff886c1dc90fa15cb2e
Patch0:		%{name}-opt.patch
Patch1:		%{name}-types.patch
URL:		http://xmoto.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel
BuildRequires:	libvorbis-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X-Moto is a challenging 2D motocross platform game, where physics play
an all important role in the gameplay. You need to control your bike
to its limit, if you want to have a chance finishing the more
difficult of the challenges.

First you'll try just to complete the levels, while later you'll
compete with yourself and others, racing against the clock.

%description -l pl
X-Moto jest wyzywaj�c� motocrossow� dwuwymiarow� gr� platformow�,
gdzie fizyka ma w rozgrywce g��wn� rol�. Panowanie nad motorem musi
by� jak najbardziej wy�y�owane, je�eli chce si� my�le� o uko�czeniu
trudniejszych poziom�w.

Z pocz�tku po prostu zalicza si� poziomy, p�niej walczy si� z
wynikami, swoimi i innych, w wy�cigu z czasem.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/xmoto
