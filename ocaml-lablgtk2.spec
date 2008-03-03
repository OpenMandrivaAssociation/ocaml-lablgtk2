%define base_name	lablgtk
%define name		ocaml-%{base_name}2
%define version		2.10.0
%define release		%mkrel 6

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	OCaml interface to the GIMP Tool Kit Version 2
Source:		http://wwwfun.kurims.kyoto-u.ac.jp/soft/olabl/dist/%{base_name}-%{version}.tar.gz
Patch0:		lablgtk-2.10.0.patch
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
Requires:	%{name} = %{version}-%{release}
Requires:	gtk2-devel

%description devel
This package contains the development files needed to build applications
using %{name}.

%prep
%setup -q -n %{base_name}-%{version}
%patch0 -p0
perl -pi -e "s/^directory.*$//" META

%build
./configure
make
make opt

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{ocaml_sitelib}/stublibs
install -d -m 755 %{buildroot}%{ocaml_sitelib}/lablgtk2/
install -m 644 META %{buildroot}%{ocaml_sitelib}/lablgtk2/
make install \
	BINDIR=%{buildroot}%{_bindir} \
	INSTALLDIR=%{buildroot}%{ocaml_sitelib}/lablgtk2 \
	DLLDIR=%{buildroot}%{ocaml_sitelib}/stublibs

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING CHANGES README
%dir %{ocaml_sitelib}/lablgtk2
%{ocaml_sitelib}/lablgtk2/*.cmi
%{ocaml_sitelib}/stublibs/*

%files devel
%defattr(-,root,root)
%{_bindir}/*
%{ocaml_sitelib}/lablgtk2/*
%exclude %{ocaml_sitelib}/lablgtk2/*.cmi
