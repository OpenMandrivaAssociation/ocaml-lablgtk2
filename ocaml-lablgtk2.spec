%define base_name	lablgtk
%define name		ocaml-%{base_name}2
%define version		2.14.2
%define release		2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	OCaml interface to the GIMP Tool Kit Version 2
Source0:	http://wwwfun.kurims.kyoto-u.ac.jp/soft/olabl/dist/%{base_name}-%{version}.tar.gz
Source1:	lablgtk-2.14.0-doc-html.tar.lzma
URL:		http://wwwfun.kurims.kyoto-u.ac.jp/soft/olabl/lablgtk.html
License:	LGPL
Group:		Development/Other
BuildRequires:	camlp4
BuildRequires:	gtk+2-devel
BuildRequires:	librsvg-devel
BuildRequires:	gnomeui2-devel	
BuildRequires:	gnome-panel-devel
BuildRequires:	gtkspell-devel
BuildRequires:	libglade2-devel
BuildRequires:	libgtksourceview-1.0-devel
BuildRequires:	libgtksourceview-2.0-devel
BuildRequires:	gtkglarea2-devel
BuildRequires:	ocaml-lablgl-devel
BuildRequires:  Mesa-common-devel
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

%package doc
Summary:	Documentation and examples for %{name}
Group:		Development/Other

%description doc
This package contains the ocamldoc generated documentation for %{name},
and some examples.


%prep
%setup -q -n %{base_name}-%{version}
perl -pi -e "s/^directory.*$//" META
sed -i -e 's/version="2.12.0"/version="%{version}"/' META
lzcat %{SOURCE1} | tar xf -
mv lablgtk-2.14.0-doc-html/ doc/

%build
%configure2_5x
make
make opt

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}/%{_bindir}
install -d -m 755 %{buildroot}/%{_libdir}/ocaml/stublibs
install -d -m 755 %{buildroot}/%{_libdir}/ocaml/lablgtk2/
install -m 644 META %{buildroot}/%{_libdir}/ocaml/lablgtk2/
make install \
	BINDIR=%{buildroot}/%{_bindir} \
	INSTALLDIR=%{buildroot}/%{_libdir}/ocaml/lablgtk2 \
	DLLDIR=%{buildroot}/%{_libdir}/ocaml/stublibs

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING CHANGES README
%{_bindir}/*
%dir %{_libdir}/ocaml/lablgtk2
%{_libdir}/ocaml/lablgtk2/META
%{_libdir}/ocaml/lablgtk2/*.cmi
%{_libdir}/ocaml/lablgtk2/*.cma
%{_libdir}/ocaml/lablgtk2/*.cmo
%{_libdir}/ocaml/lablgtk2/*.o
%{_libdir}/ocaml/stublibs/*

%files devel
%defattr(-,root,root)
%{_libdir}/ocaml/lablgtk2/*
%exclude %{_libdir}/ocaml/lablgtk2/META
%exclude %{_libdir}/ocaml/lablgtk2/*.cmi
%exclude %{_libdir}/ocaml/lablgtk2/*.cma
%exclude %{_libdir}/ocaml/lablgtk2/*.cmo
%exclude %{_libdir}/ocaml/lablgtk2/*.o

%files doc
%defattr(-,root,root)
%doc examples
%doc doc

