%define api %(echo %{version}|cut -d. -f1)
%define major %api
%define beta %nil

%define qtquicktest %mklibname qt%{api}quicktest %{api}
%define qtquicktestd %mklibname qt%{api}quicktest -d
%define quicktest_p_d %mklibname qt%{api}quicktest-private -d

%define qtquick %mklibname qt%{api}quick %{major}
%define qtquickd %mklibname qt%{api}quick -d
%define qtquick_p_d %mklibname qt%{api}quick-private -d

%define qtquickwidgets %mklibname qt%{api}quickwidgets %{major}
%define qtquickwidgetsd %mklibname qt%{api}quickwidgets -d
%define qtquickwidgetsd_p_d %mklibname qt%{api}quickwidgets-private -d

%define qtquickparticles %mklibname qt%{api}quickparticles %{major}
%define qtquickparticlesd %mklibname qt%{api}quickparticles -d
%define qtquickparticles_p_d %mklibname qt%{api}quickparticles-private -d

%define qtqml %mklibname qt%{api}qml %{major}
%define qtqmld %mklibname qt%{api}qml -d
%define qtqml_p_d %mklibname qt%{api}qml-private -d

%define _qt_prefix %{_libdir}/qt%{api}
%define _disable_lto 1

Name:		qt5-qtdeclarative
Version:	5.5.0
%if "%{beta}" != ""
Release:	1.%{beta}.1
%define qttarballdir qtdeclarative-opensource-src-%{version}-%{beta}
Source0:	http://download.qt.io/development_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}-%{beta}/submodules/%{qttarballdir}.tar.xz
%else
Release:	3
%define qttarballdir qtdeclarative-opensource-src-%{version}
Source0:	http://download.qt.io/official_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}/submodules/%{qttarballdir}.tar.xz
%endif
Summary:	Qt GUI toolkit
Group:		Development/KDE and Qt
License:	LGPLv2 with exceptions or GPLv3 with exceptions and GFDL
URL:		http://www.qt.io
BuildRequires:	pkgconfig(Qt5Core) = %{version}
BuildRequires:	qt5-qtbase-devel = %{version}
BuildRequires:	pkgconfig(Qt5Network) = %{version}
BuildRequires:	pkgconfig(Qt5Sql) = %{version}
BuildRequires:	pkgconfig(Qt5Gui) = %{version}
BuildRequires:	pkgconfig(Qt5Test) = %{version}
BuildRequires:	pkgconfig(Qt5Widgets) = %{version}
BuildRequires:	pkgconfig(Qt5XmlPatterns) = %{version}

%description
Qt is a GUI software toolkit which simplifies the task of writing and
maintaining GUI (Graphical User Interface) applications for the X
Window System. Qt is written in C++ and is fully object-oriented.

%files
%_qt5_bindir/qml
%_qt5_bindir/qmlimportscanner
%_qt5_bindir/qmlmin
%_qt5_bindir/qmlplugindump
%_qt5_bindir/qmlprofiler
%_qt5_bindir/qmlscene
%_qt5_bindir/qmltestrunner
%_qt5_bindir/qmleasing
%_qt5_bindir/qmllint
%_qt_prefix/qml/QtTest
%_qt_prefix/qml/QtQuick*
%_qt_prefix/plugins/qmltooling/libqmldbg_qtquick2.so
%_qt_prefix/plugins/qmltooling/libqmldbg_tcp.so
%_qt_prefix/qml/Qt/labs/folderlistmodel
%_qt_prefix/qml/Qt/labs/settings

#------------------------------------------------------------------------------

%package -n %{qtquicktest}
Summary: Qt%{api} Lib
Group: System/Libraries

%description -n %{qtquicktest}
Qt%{api} Lib.

%files -n %{qtquicktest}
%{_qt5_libdir}/libQt5QuickTest.so.%{api}*

#------------------------------------------------------------------------------

%package -n %{qtquicktestd}
Summary: Devel files needed to build apps based on QtVersit
Group:    Development/KDE and Qt
Requires: %{qtquicktest} = %version
Requires: %{name} = %version

%description -n %{qtquicktestd}
Devel files needed to build apps based on QtVersit.

%files -n %{qtquicktestd}
%_qt5_libdir/libQt5QuickTest.prl
%_qt5_libdir/libQt5QuickTest.so
%_qt5_libdir/cmake/Qt5QuickTest
%_qt5_includedir/QtQuickTest
%exclude %_qt5_includedir/QtQuickTest/%version
%_qt5_libdir/pkgconfig/Qt5QuickTest.pc
%_qt_prefix/examples/qmltest

#------------------------------------------------------------------------------

%package -n %{quicktest_p_d}
Summary: Devel files needed to build apps based on QtVersit
Group:    Development/KDE and Qt
Requires: %{qtquicktestd} = %version
Provides: qt5-quicktest-private-devel = %version

%description -n %{quicktest_p_d}
Devel files needed to build apps based on QtVersit.

%files -n %{quicktest_p_d}
%_qt5_includedir/QtQuickTest/%version

#------------------------------------------------------------------------------

%package -n %{qtquick}
Summary: Qt%{api} Lib
Group: System/Libraries

%description -n %{qtquick}
Qt%{api} Lib.

%files -n %{qtquick}
%{_qt5_libdir}/libQt5Quick.so.%{api}*
%{_qt_prefix}/qml/QtQml

#------------------------------------------------------------------------------

%package -n %{qtquickd}
Summary: Devel files needed to build apps based on QtVersit
Group:    Development/KDE and Qt
Requires: %{name} = %version
Requires: %{qtquick} = %version

%description -n %{qtquickd}
Devel files needed to build apps based on QtVersit.

%files -n %{qtquickd}
%_qt5_libdir/libQt5Quick.prl
%_qt5_libdir/libQt5Quick.so
%_qt5_libdir/cmake/Qt5Quick
%_qt5_includedir/QtQuick
%exclude %_qt5_includedir/QtQuick/%version
%_qt_prefix/examples/quick
%_qt5_libdir/pkgconfig/Qt5Quick.pc
%_qt_prefix/mkspecs/modules/qt_lib_quick.pri
#_qt5_libdir/cmake/Qt5Widgets/Qt5Widgets_AccessibleQuickFactory.cmake

#------------------------------------------------------------------------------

%package -n %{qtquick_p_d}
Summary: Devel files needed to build apps based on QtVersit
Group:    Development/KDE and Qt
Requires: %{qtquickd} = %version
Requires: %{qtqml_p_d} = %version
Provides: qt5-qtquick-private-devel = %version

%description -n %{qtquick_p_d}
Devel files needed to build apps based on QtVersit.

%files -n %{qtquick_p_d}
%_qt5_includedir/QtQuick/%version
%_qt_prefix/mkspecs/modules/qt_lib_quick_private.pri

#------------------------------------------------------------------------------

%package -n %{qtquickwidgets}
Summary: Qt%{api} Lib 
Group: System/Libraries

%description -n %{qtquickwidgets}
Qt%{api} Lib.

%files -n %{qtquickwidgets}
%{_qt5_libdir}/libQt5QuickWidgets.so.%{api}*

#------------------------------------------------------------------------------

%package -n %{qtquickwidgetsd}
Summary: Devel files needed to build apps based on QtVersit
Group:    Development/KDE and Qt
Requires: %{name} = %version
Requires: %{qtquickwidgets} = %version

%description -n %{qtquickwidgetsd}
Devel files needed to build apps based on QtVersit.

%files -n %{qtquickwidgetsd}
%_qt5_libdir/libQt5QuickWidgets.prl
%_qt5_libdir/libQt5QuickWidgets.so
%_qt5_libdir/cmake/Qt5QuickWidgets
%_qt5_includedir/QtQuickWidgets
%exclude %_qt5_includedir/QtQuickWidgets/%version
%_qt5_libdir/pkgconfig/Qt5QuickWidgets.pc
%_qt_prefix/mkspecs/modules/qt_lib_quickwidgets.pri

#------------------------------------------------------------------------------

%package -n %{qtquickwidgetsd_p_d}
Summary: Devel files needed to build apps based on QtVersit
Group:    Development/KDE and Qt
Requires: %{qtquickwidgetsd} = %version
Requires: %{qtqml_p_d} = %version
Provides: qt5-qtquickwidgets-private-devel = %version

%description -n %{qtquickwidgetsd_p_d}
Devel files needed to build apps based on QtVersit.

%files -n %{qtquickwidgetsd_p_d}
%_qt5_includedir/QtQuickWidgets/%version
%_qt_prefix/mkspecs/modules/qt_lib_quickwidgets_private.pri

#------------------------------------------------------------------------------

%package -n %{qtquickparticles}
Summary: Qt%{api} Lib
Group: System/Libraries

%description -n %{qtquickparticles}
Qt%{api} Lib.

%files -n %{qtquickparticles}
%{_qt5_libdir}/libQt5QuickParticles.so.%{api}*

#------------------------------------------------------------------------------

%package -n %{qtquickparticlesd}
Summary: Devel files needed to build apps based on QtVersit
Group:    Development/KDE and Qt
Requires: %{name} = %version
Requires: %{qtquickparticles} = %version

%description -n %{qtquickparticlesd}
Devel files needed to build apps based on QtVersit.

%files -n %{qtquickparticlesd}
%_qt5_libdir/libQt5QuickParticles.prl
%_qt5_libdir/libQt5QuickParticles.so
%_qt5_includedir/QtQuickParticles
%exclude %_qt5_includedir/QtQuickParticles/%version
%_qt5_libdir/pkgconfig/Qt5QuickParticles.pc

#------------------------------------------------------------------------------

%package -n %{qtquickparticles_p_d}
Summary: Devel files needed to build apps based on QtVersit
Group:    Development/KDE and Qt
Requires: %{qtquickparticlesd} = %version
Provides: qt5-qtquickparticles-private-devel = %version

%description -n %{qtquickparticles_p_d}
Devel files needed to build apps based on QtVersit.

%files -n %{qtquickparticles_p_d}
%_qt5_includedir/QtQuickParticles/%version
%_qt_prefix/mkspecs/modules/qt_lib_quickparticles_private.pri

#------------------------------------------------------------------------------

%package -n %{qtqml}
Summary: Qt%{api} Lib
Group: System/Libraries

%description -n %{qtqml}
Qt%{api} Lib.

%files -n %{qtqml}
%{_qt5_libdir}/libQt5Qml.so.%{api}*

#------------------------------------------------------------------------------

%package -n %{qtqmld}
Summary: Devel files needed to build apps based on QtVersit
Group:    Development/KDE and Qt
Requires: %{name} = %version
Requires: %{qtqml} = %version
Requires: pkgconfig(Qt5Core) = %version
Requires: pkgconfig(Qt5Network) = %version

%description -n %{qtqmld}
Devel files needed to build apps based on QtVersit.

%files -n %{qtqmld}
%_qt5_libdir/libQt5Qml.prl
%_qt5_libdir/libQt5Qml.so
%_qt5_libdir/cmake/Qt5Qml
%_qt_prefix/mkspecs/modules/qt_lib_qmltest.pri
%_qt_prefix/mkspecs/modules/qt_lib_qml.pri
%_qt_prefix/examples/qml
%_qt5_libdir/pkgconfig/Qt5Qml.pc
%_qt5_libdir/pkgconfig/Qt5QmlDevTools.pc
%_qt5_includedir/QtQml*
%exclude %_qt5_includedir/QtQml/%version
%_qt5_libdir/libQt5QmlDevTools.prl

#------------------------------------------------------------------------------

%package -n	%{qtqml_p_d}
Summary:	Devel files needed to build apps based on QtVersit
Group:		Development/KDE and Qt
Requires:	%{qtqmld} = %version
Provides:	qt5-qtqml-private-devel = %version
Requires:	pkgconfig(Qt5Core) = %version

%description -n %{qtqml_p_d}
Devel files needed to build apps based on QtVersit.

%files -n %{qtqml_p_d}
%_qt5_includedir/QtQml/%version
%_qt_prefix/mkspecs/modules/qt_lib_qml_private.pri
%_qt_prefix/mkspecs/modules/qt_lib_qmldevtools_private.pri
%_qt_prefix/mkspecs/modules/qt_lib_qmltest_private.pri

#------------------------------------------------------------------------------

%prep
%setup -q -n %qttarballdir
%apply_patches

%build
%qmake_qt5

#------------------------------------------------------------------------------
%make

%install
%makeinstall_std INSTALL_ROOT=%{buildroot}

## .prl/.la file love
# nuke .prl reference(s) to %%buildroot, excessive (.la-like) libs
pushd %{buildroot}%{_qt5_libdir}
for prl_file in libQt5*.prl ; do
  sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" ${prl_file}
  if [ -f "$(basename ${prl_file} .prl).so" ]; then
    rm -fv "$(basename ${prl_file} .prl).la"
    sed -i -e "/^QMAKE_PRL_LIBS/d" ${prl_file}
  fi
done
popd

# .la and .a files, die, die, die.
rm -f %{buildroot}%{_qt5_libdir}/lib*.la
rm -f %{buildroot}%{_qt5_libdir}/lib*.a
