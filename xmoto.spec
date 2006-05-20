Summary:	Clone of across/elma games
Summary(pl):	Klon gry across/elma
Name:		xmoto
Version:	0.1.14
Release:	1
License:	GPL
Group:		X11/Applications/Games
#Source0:	http://mesh.dl.sourceforge.net/sourceforge/xmoto/%{name}-%{version}-src.tar.gz
Source0:	http://surfnet.dl.sourceforge.net/sourceforge/xmoto/%{name}-%{version}-src.tar.gz
# Source0-md5:	f2826bd3cc19daba25a6bdf92b1d6461
Source1:	%{name}.png
Source2:	%{name}.desktop
URL:		http://xmoto.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	lua50-devel
BuildRequires:	ode-devel
BuildRequires:	pkgconfig
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

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}

%configure
%{__make} \
	GL_LIBS="-lGL"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/xmoto
%{_pixmapsdir}/*
%{_desktopdir}/*
