Summary:        MonoDevelop python Addin
Name:           monodevelop-python
Version:        2.8.1
Release:        1%{?dist}.R
License:        GPLv2+
Group:          Development/Tools
Source:         http://download.mono-project.com/sources/%{name}/%{name}-%{version}.tar.bz2
URL:            http://www.monodevelop.com

BuildRequires:  mono-devel >= 2.6
BuildRequires:  monodevelop-devel >= 2.4
BuildRequires:  mono-addins-devel
BuildRequires:  gtk-sharp2-devel
BuildRequires:  gnome-desktop-sharp-devel
Requires:       monodevelop >= 2.4


%description
Python Addin for MonoDevelop.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release} pkgconfig
Group:          Development/Libraries

%description devel
Development package for %{name}

%prep
%setup -q
##sed magic to get rid of all of the silly $prefix/lib stuff
find . -name Makefile -or -name Makefile.in -or -name Makefile.am -or -name configure -or -name configure.in -or -name \*.pc.in \
       -or -name \*.in -or -name \*.xml -or -name Makefile.include \
       | while read f ;
         do
           sed -i -e 's!$(prefix)/lib/!%{_libdir}/!' "$f"
           sed -i -e 's!@prefix@/lib/!%{_libdir}/!' "$f"
           sed -i -e 's!/usr/lib/!%{_libdir}/!' "$f"
           sed -i -e 's!${exec_prefix}/lib/!%{_libdir}/!' "$f" ;
         done

%build
./configure --prefix=%{_prefix} --bindir=%{_bindir} --datadir=%{_datadir} --libdir=%{_libdir}
make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_libdir}/monodevelop/AddIns/PyBinding/PyBinding*

%files devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/monodevelop-pybinding.pc

%changelog
* Wed Oct 26 2011 - Vasiliy N. Glazov <vascom2@gmail.com> - 2.8.1-1.R
- Update to 2.8.1

* Fri Jun 18 2010 - Claudio Rodrigo Pereyra Diaz <claudio@pereyradiaz.com.ar> - 2.4
- Update upstream version

* Fri Feb 12 2010 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.2-1
- Initial import
