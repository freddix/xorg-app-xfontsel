Summary:	xfontsel application - point and click selection of X11 font names
Name:		xorg-app-xfontsel
Version:	1.0.4
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xfontsel-%{version}.tar.bz2
# Source0-md5:	3f7e8ba9e34589a07d190575ae6c86cf
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pkg-config
BuildRequires:	xorg-libXaw-devel
BuildRequires:	xorg-libXmu-devel
BuildRequires:	xorg-libXt-devel
BuildRequires:	xorg-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The xfontsel application provides a simple way to display the fonts
known to your X server, examine samples of each, and retrieve the X
Logical Font Description (XLFD) full name for a font.

%prep
%setup -qn xfontsel-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
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
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/xfontsel
%{_datadir}/X11/app-defaults/XFontSel
%{_mandir}/man1/xfontsel.1x*

