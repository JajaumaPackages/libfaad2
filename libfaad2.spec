Name:           libfaad2
Version:        2.7
Release:        1%{?dist}
Summary:        An open source MPEG-4 and MPEG-2 AAC decoder

License:        GPLv2+
URL:            http://www.audiocoding.com/faad2.html
Source0:        http://downloads.sourceforge.net/sourceforge/faac/faad2-%{version}.tar.bz2

%description
FAAD2 is a HE, LC, MAIN and LTP profile, MPEG2 and MPEG-4 AAC decoder. FAAD2 
includes code for SBR (HE AAC) decoding. FAAD2 is licensed under the GPL.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        -n faad2
Summary:        FAAD2 cli decoder

%description    -n faad2
This package contains the FAAD2 frontend decoder.


%prep
%setup -q -n faad2-%{version}


%build
%configure --disable-static

sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}


%install
rm -rf %{buildroot}
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'
%{__rm} %{buildroot}%{_includedir}/mp4ff{,int}.h
%{__rm} %{buildroot}%{_libdir}/libmp4ff.a
install -dm755 %{buildroot}%{_mandir}/man1
%{__mv} %{buildroot}%{_mandir}/{manm/faad.man,man1/faad.1}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc AUTHORS ChangeLog COPYING NEWS README*
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so

%files -n faad2
%{_bindir}/*
%{_mandir}/man1/*


%changelog
* Wed Aug 10 2016 Jajauma's Packages <jajauma@yandex.ru> - 2.7-1
- Public release
