%define base_name lablgtk

Summary:	OCaml interface to the GIMP Tool Kit Version 2
Name:		ocaml-%{base_name}2
Version:	2.18.4
Release:	1
License:	LGPLv2.1+
Group:		Development/Other
Url:		http://lablgtk.forge.ocamlcore.org/
Source0:	http://wwwfun.kurims.kyoto-u.ac.jp/soft/olabl/dist/%{base_name}-%{version}.tar.gz
Source1:	lablgtk-2.14.0-doc-html.tar.lzma
BuildRequires:	camlp4
BuildRequires:	ocaml-findlib
BuildRequires:	ocaml-lablgl-devel
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtkgl-2.0)
BuildRequires:	pkgconfig(gtksourceview-1.0)
BuildRequires:	pkgconfig(gtksourceview-2.0)
BuildRequires:	pkgconfig(gtkspell-2.0)
BuildRequires:	pkgconfig(libglade-2.0)
BuildRequires:	pkgconfig(libgnomeui-2.0)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(pangocairo)
BuildRequires:	ocaml-camlp4-devel

%description
OCaml interface to the GIMP Tool Kit Version 2.

%files
%doc COPYING CHANGES README
%{_bindir}/*
%dir %{_libdir}/ocaml/lablgtk2
%{_libdir}/ocaml/lablgtk2/META
%{_libdir}/ocaml/lablgtk2/*.cmi
%{_libdir}/ocaml/lablgtk2/*.cma
%{_libdir}/ocaml/lablgtk2/*.cmo
%{_libdir}/ocaml/lablgtk2/*.o
%{_libdir}/ocaml/stublibs/*

#----------------------------------------------------------------------------

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{EVRD}
Requires:	pkgconfig(gtk+-2.0)

%description devel
This package contains the development files needed to build applications
using %{name}.

%files devel
%{_libdir}/ocaml/lablgtk2/*
%exclude %{_libdir}/ocaml/lablgtk2/META
%exclude %{_libdir}/ocaml/lablgtk2/*.cmi
%exclude %{_libdir}/ocaml/lablgtk2/*.cma
%exclude %{_libdir}/ocaml/lablgtk2/*.cmo
%exclude %{_libdir}/ocaml/lablgtk2/*.o

#----------------------------------------------------------------------------

%package doc
Summary:	Documentation and examples for %{name}
Group:		Development/Other

%description doc
This package contains the ocamldoc generated documentation for %{name},
and some examples.

%files doc
%doc examples
%doc doc

#----------------------------------------------------------------------------

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
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
install -d -m 755 %{buildroot}%{_libdir}/ocaml/stublibs
make install \
	RANLIB=true \
	BINDIR=%{buildroot}/%{_bindir} \
	LIBDIR=%{buildroot}/%{_libdir}/ocaml/lablgtk2 \
	INSTALLDIR=%{buildroot}/%{_libdir}/ocaml/lablgtk2 \
	DLLDIR=%{buildroot}/%{_libdir}/ocaml/stublibs

for cmo in $(find src/ -type f -name "*.cmo"); do
    %{__install} -m0644 -D $cmo %{buildroot}/%{_libdir}/ocaml/lablgtk2/`basename $cmo`
done;

rm -f %{buildroot}%{_libdir}/ocaml/ld.conf
