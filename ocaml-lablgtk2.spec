%define base_name lablgtk

Name:		ocaml-%{base_name}2
Version:	2.16.0
Release:	4
Summary:	OCaml interface to the GIMP Tool Kit Version 2
Source0:	http://wwwfun.kurims.kyoto-u.ac.jp/soft/olabl/dist/%{base_name}-%{version}.tar.gz
Source1:	lablgtk-2.14.0-doc-html.tar.lzma
URL:		http://lablgtk.forge.ocamlcore.org/
License:	LGPL
Group:		Development/Other
BuildRequires:	camlp4
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(libgnomeui-2.0)
BuildRequires:	pkgconfig(libpanelapplet-4.0)
BuildRequires:	pkgconfig(gtkspell-2.0)
BuildRequires:	pkgconfig(libglade-2.0)
BuildRequires:	pkgconfig(gtksourceview-1.0)
BuildRequires:	pkgconfig(gtksourceview-2.0)
BuildRequires:	pkgconfig(gtkgl-2.0)
BuildRequires:	ocaml-lablgl-devel
BuildRequires:  mesa-common-devel

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

for cmo in $(find src/ -type f -name "*.cmo"); do
	%{__install} -m0644 -D $cmo %{buildroot}/%{_libdir}/ocaml/lablgtk2/`basename $cmo`
done;

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


%changelog
* Fri Jun 08 2012 Bernhard Rosenkraenzer <bero@bero.eu> 2.14.2-4
+ Revision: 803316
- Fix build in current environment
- Don't BuildRequire 32bit libraries on x86_64
- Clean up spec file

* Sat Sep 17 2011 Alexandre Lissy <alissy@mandriva.com> 2.14.2-3
+ Revision: 700156
- Installing .cmo files, pango.cmo at least is needed by ocaml-cairo
- Release bump, rebuilding for latest ocaml release

* Wed Oct 06 2010 Funda Wang <fwang@mandriva.org> 2.14.2-1mdv2011.0
+ Revision: 583596
- New version 2.14.2

* Fri Sep 25 2009 Florent Monnier <blue_prawn@mandriva.org> 2.14.0-2mdv2010.0
+ Revision: 449212
- added the documentation

* Fri Sep 25 2009 Florent Monnier <blue_prawn@mandriva.org> 2.14.0-1mdv2010.0
+ Revision: 449176
- new version 2.14.0
- new version 2.14.0

* Wed Sep 23 2009 Florent Monnier <blue_prawn@mandriva.org> 2.12.0-9mdv2010.0
+ Revision: 447866
- included the examples, and corrected the version in the META file

* Wed Sep 23 2009 Florent Monnier <blue_prawn@mandriva.org> 2.12.0-8mdv2010.0
+ Revision: 447566
- the gtksourceview module requires version 1.0 of the lib, 2.0 is in the svn

* Tue Sep 22 2009 Florent Monnier <blue_prawn@mandriva.org> 2.12.0-7mdv2010.0
+ Revision: 447521
- fixed gtkglarea deps
- BuildRequires: gtksourceview-devel and BuildRequires: ocaml-lablgl-devel

* Mon Jul 27 2009 Florent Monnier <blue_prawn@mandriva.org> 2.12.0-6mdv2010.0
+ Revision: 400484
- corrected libglade dependency

* Sat Jun 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.12.0-5mdv2010.0
+ Revision: 390044
- rebuild
- rebuild

* Wed Jan 07 2009 Florent Monnier <blue_prawn@mandriva.org> 2.12.0-3mdv2009.1
+ Revision: 326787
- sources for lablgtk-2.10.1
- new version lablgtk-2.10.1
- patch to add an include for libgnomeui
- fixed a header include for libgnomeui
- move non-devel files in main package
- site-lib hierarchy doesn't exist anymore

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 2.10.1-3mdv2009.0
+ Revision: 254266
- rebuild

* Mon Mar 03 2008 Stefan van der Eijk <stefan@mandriva.org> 2.10.1-1mdv2008.1
+ Revision: 178128
- 2.10.1
- rebuild for ocaml

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Thu Dec 20 2007 Guillaume Bedot <littletux@mandriva.org> 2.10.0-5mdv2008.1
+ Revision: 135369
- patch fixing locale issues

* Wed Dec 19 2007 Guillaume Bedot <littletux@mandriva.org> 2.10.0-4mdv2008.1
+ Revision: 133742
- fix META file.

* Mon Dec 17 2007 Guillaume Bedot <littletux@mandriva.org> 2.10.0-3mdv2008.1
+ Revision: 131036
- also include META so ocamlfind works

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Dec 17 2007 Guillaume Bedot <littletux@mandriva.org> 2.10.0-2mdv2008.1
+ Revision: 123007
- back to ocaml policy compliance

* Fri Nov 30 2007 Guillaume Bedot <littletux@mandriva.org> 2.10.0-1mdv2008.1
+ Revision: 114195
- 2.10.0
- fixed location of caml archives

* Sat Sep 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.6.0-10mdv2008.0
+ Revision: 77689
- ocaml policy compliance


* Thu Jan 25 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.6.0-9mdv2007.0
+ Revision: 113157
- rebuild for new ocaml
- Import ocaml-lablgtk2

* Tue Aug 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.6.0-8mdv2007.0
- Rebuild

* Wed Apr 26 2006 Pixel <pixel@mandriva.com> 2.6.0-7mdk
- rebuild for new ocaml

* Thu Jan 26 2006 Pixel <pixel@mandriva.com> 2.6.0-6mdk
- only the stublibs are non-devel stuff (ie not requiring ocaml)

* Mon Jan 23 2006 Pixel <pixel@mandriva.com> 2.6.0-5mdk
- rebuild for new ocaml

* Fri Jan 13 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.6.0-4mdk
- devel packages requires gtk+2-devel

* Wed Nov 09 2005 Guillaume Bedot <littletux@mandriva.org> 2.6.0-3mdk
- rebuild for new lablgl

* Mon Nov 07 2005 Pixel <pixel@mandriva.com> 2.6.0-2mdk
- rebuild for new ocaml

* Wed Nov 02 2005 Guillaume Rousse <guillomovitch@mandriva.org> 2.6.0-1mdk
- %%mkrel
- Anssi Hannula <anssi.hannula@gmail.com>
 - 2.6.0

* Tue Nov 01 2005 Frederic Lepied <flepied@mandriva.com> 2.4.1-0.20050701.2mdk
- rebuild to compile gtkgl support

* Wed Jul 20 2005 Guillaume Rousse <guillomovitch@mandriva.org> 2.4.1-0.20050701.1mdk 
- new snapshot
- more buildrequires
- remove merged rpm macros

* Wed May 18 2005 Laurent Culioli <laurent@mandriva.org> 2.4.1-0.20050218.1mdk
- 20050218

* Fri Apr 22 2005 Guillaume Rousse <guillomovitch@mandriva.org> 2.4.0-1mdk 
- contributed by Julien Narboux (Julien.Narboux@inria.fr)

