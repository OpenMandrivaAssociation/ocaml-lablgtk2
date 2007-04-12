%define base_name	lablgtk
%define name		ocaml-%{base_name}2
%define version		2.6.0
%define release		%mkrel 9

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	OCaml interface to the GIMP Tool Kit Version 2
Source:		http://wwwfun.kurims.kyoto-u.ac.jp/soft/olabl/dist/%{base_name}-%{version}.tar.bz2
URL:		http://wwwfun.kurims.kyoto-u.ac.jp/soft/olabl/lablgtk.html
License:	LGPL
Group:		Development/Other
BuildRequires:	camlp4
BuildRequires:	gtk+2-devel
BuildRequires:	gtkglarea2-devel
BuildRequires:	librsvg-devel
BuildRequires:	gnomeui2-devel	
BuildRequires:	gnome-panel-devel
BuildRequires:	gtkspell-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
OCaml interface to the GIMP Tool Kit Version 2.

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{version}
Requires:	gtk2-devel

%description devel
This package contains the development files needed to build applications
using %{name}.

%prep
%setup -q -n %{base_name}-%{version}

%build
./configure
make
make opt

%install
rm -rf %{buildroot}
destdir=`ocamlc -where`
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}$destdir/stublibs
make install \
	BINDIR=%{buildroot}%{_bindir} \
	INSTALLDIR=%{buildroot}$destdir/lablgtk2 \
	DLLDIR=%{buildroot}$destdir/stublibs

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING
%{_libdir}/ocaml/stublibs/*

%files devel
%defattr(-,root,root)
%doc CHANGES README
%{_bindir}/*
%{_libdir}/ocaml/lablgtk2


