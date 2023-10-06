%define api %(echo %{version}|cut -d. -f1)
%define major %api
%define beta %{nil}

%define qtquicktest %mklibname qt%{api}quicktest %{api}
%define qtquicktestd %mklibname qt%{api}quicktest -d
%define quicktest_p_d %mklibname qt%{api}quicktest-private -d

%define qtquick %mklibname qt%{api}quick %{major}
%define qtquickd %mklibname qt%{api}quick -d
%define qtquick_p_d %mklibname qt%{api}quick-private -d

%define qtquickshapes %mklibname qt%{api}quickshapes %{major}
%define qtquickshapesd %mklibname qt%{api}quickshapes -d
%define qtquickshapes_p_d %mklibname qt%{api}quickshapes-private -d

%define qtquickwidgets %mklibname qt%{api}quickwidgets %{major}
%define qtquickwidgetsd %mklibname qt%{api}quickwidgets -d
%define qtquickwidgetsd_p_d %mklibname qt%{api}quickwidgets-private -d

%define qtquickparticles %mklibname qt%{api}quickparticles %{major}
%define qtquickparticlesd %mklibname qt%{api}quickparticles -d
%define qtquickparticles_p_d %mklibname qt%{api}quickparticles-private -d

%define qtqml %mklibname qt%{api}qml %{major}
%define qtqmld %mklibname qt%{api}qml -d
%define qtqml_p_d %mklibname qt%{api}qml-private -d

%define qtqmlmodels %mklibname qt%{api}qmlmodels %{major}
%define qtqmlmodelsd %mklibname qt%{api}qmlmodels -d
%define qtqmlmodels_p_d %mklibname qt%{api}qmlmodels-private -d

%define qtqmlworkerscript %mklibname qt%{api}qmlworkerscript %{major}
%define qtqmlworkerscriptd %mklibname qt%{api}qmlworkerscript -d
%define qtqmlworkerscript_p_d %mklibname qt%{api}qmlworkerscript-private -d

%define _qt_prefix %{_libdir}/qt%{api}

%global optflags %{optflags} -O3

Summary:	Qt GUI toolkit
Name:		qt5-qtdeclarative
Group:		Development/KDE and Qt
License:	LGPLv2 with exceptions or GPLv3 with exceptions and GFDL
URL:		http://www.qt.io
Version:	5.15.11
%if "%{beta}" != ""
Release:	0.%{beta}.1
%define qttarballdir qtdeclarative-everywhere-src-%{version}-%{beta}
Source0:	http://download.qt.io/development_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}-%{beta}/submodules/%{qttarballdir}.tar.xz
%else
Release:	1
%define qttarballdir qtdeclarative-everywhere-opensource-src-%{version}
Source0:	http://download.qt.io/official_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}/submodules/%{qttarballdir}.tar.xz
%endif
# (tpg) fix build ../3rdparty/masm/yarr/YarrPattern.cpp:39:29: fatal error: RegExpJitTables.h: No such file or directory
Patch1:		qtdeclarative-everywhere-src-5.6.0-fix-build.patch
# (bero) more build fixes
Patch2:		qt5-qtdeclarative-buildfixes.patch
Patch3:		qtdeclarative-python3.patch
# (tpg) https://bugreports.qt.io/browse/QTBUG-83890
Patch4:		qtdeclarative-5.14.2-QQuickItemView-fix-maxXY-extent.patch
# from KDE https://invent.kde.org/qt/qt/qtdeclarative -b kde/5.15
Patch1001:	0001-Remove-unused-QPointer-QQuickPointerMask.patch
Patch1002:	0002-QQmlDelegateModel-Refresh-the-view-when-a-column-is-.patch
Patch1003:	0003-Fix-TapHandler-so-that-it-actually-registers-a-tap.patch
Patch1004:	0004-Revert-Fix-TapHandler-so-that-it-actually-registers-.patch
Patch1005:	0005-Make-sure-QQuickWidget-and-its-offscreen-window-s-sc.patch
Patch1006:	0006-QQuickItem-Guard-against-cycles-in-nextPrevItemInTab.patch
Patch1007:	0007-Don-t-convert-QByteArray-in-startDrag.patch
Patch1008:	0008-Fix-build-after-95290f66b806a307b8da1f72f8fc2c698019.patch
Patch1009:	0009-Implement-accessibility-for-QQuickWidget.patch
Patch1010:	0010-Send-ObjectShow-event-for-visible-components-after-i.patch
Patch1011:	0011-QQuickItem-avoid-emitting-signals-during-destruction.patch
Patch1012:	0012-a11y-track-item-enabled-state.patch
Patch1013:	0013-Make-QaccessibleQuickWidget-private-API.patch
Patch1014:	0014-Qml-Don-t-crash-when-as-casting-to-type-with-errors.patch
Patch1015:	0015-QQmlImportDatabase-Make-sure-the-newly-added-import-.patch
Patch1016:	0016-QQuickState-when-handle-QJSValue-properties-correctl.patch
Patch1017:	0017-Models-Avoid-crashes-when-deleting-cache-items.patch
Patch1018:	0018-qv4function-Fix-crash-due-to-reference-being-invalid.patch
Patch1019:	0019-Quick-Animations-Fix-crash.patch
Patch1020:	0020-Prevent-crash-when-destroying-asynchronous-Loader.patch
Patch1021:	0021-QQuickItem-Fix-effective-visibility-for-items-withou.patch
Patch1022:	0022-Revert-QQuickItem-Fix-effective-visibility-for-items.patch
Patch1023:	0023-Accessibility-respect-value-in-attached-Accessible-i.patch
Patch1024:	0024-qml-tool-Use-QCommandLineParser-process-rather-than-.patch
Patch1025:	0025-JIT-Add-missing-STORE-LOAD-_ACC-to-CreateCallContext.patch
Patch1026:	0026-QQmlJs-MemoryPool-fix-potential-UB-pointer-overflow.patch
Patch1027:	0027-QRecyclePool-fix-potential-UB.patch
Patch1028:	0028-QtQml-Clean-up-QQmlData-ctor.patch
Patch1029:	0029-QML-Make-notify-list-thread-safe.patch
Patch1030:	0030-Flickable-prevent-fixup-from-being-called-while-drag.patch

BuildRequires:	pkgconfig(Qt5Core) = %{version}
BuildRequires:	qmake5 = %{version}
BuildRequires:	pkgconfig(Qt5Network) = %{version}
BuildRequires:	pkgconfig(Qt5Sql) = %{version}
BuildRequires:	pkgconfig(Qt5Gui) = %{version}
BuildRequires:	pkgconfig(Qt5Test) = %{version}
BuildRequires:	pkgconfig(Qt5Widgets) = %{version}
BuildRequires:	pkgconfig(Qt5OpenGL) = %{version}
BuildRequires:	pkgconfig(Qt5Xml) = %{version}
BuildRequires:	ruby
BuildRequires:	byacc
BuildRequires:	bison
# For code generator in yarr
BuildRequires:	python
BuildRequires:	qlalr5
# For the Provides: generator
BuildRequires:	cmake >= 3.11.0-1
Conflicts:	qt5-qtquickcontrols < 5.8.0
# Not currently picked up by the dep generator, maybe
# there's some internal hardcodes
Provides:	qml(QtQuick) = 2.14
Provides:	qml(QtQuick.tooling) = 1.2
Provides:	qml(QtQuick.Window) = 2.1

%description
Qt is a GUI software toolkit which simplifies the task of writing and
maintaining GUI (Graphical User Interface) applications for the X
Window System. Qt is written in C++ and is fully object-oriented.

%files
%{_qt5_bindir}/qml
%{_qt5_bindir}/qmlcachegen
%{_qt_prefix}/mkspecs/features/qmlcache.prf
%{_qt5_bindir}/qmlimportscanner
%{_qt5_bindir}/qmlmin
%{_qt5_bindir}/qmlplugindump
%{_qt5_bindir}/qmlpreview
%{_qt5_bindir}/qmlprofiler
%{_qt5_bindir}/qmlscene
%{_qt5_bindir}/qmltestrunner
%{_qt5_bindir}/qmleasing
%{_qt5_bindir}/qmllint
%{_qt5_bindir}/qmltime
%{_qt_prefix}/qml/QtTest
%{_qt_prefix}/qml/QtQuick*
%{_qt_prefix}/qml/builtins.qmltypes
%dir %{_qt_prefix}/plugins/qmltooling
%{_qt_prefix}/plugins/qmltooling/libqmldbg_debugger.so
%{_qt_prefix}/plugins/qmltooling/libqmldbg_inspector.so
%{_qt_prefix}/plugins/qmltooling/libqmldbg_local.so
%{_qt_prefix}/plugins/qmltooling/libqmldbg_native.so
%{_qt_prefix}/plugins/qmltooling/libqmldbg_profiler.so
%{_qt_prefix}/plugins/qmltooling/libqmldbg_quickprofiler.so
%{_qt_prefix}/plugins/qmltooling/libqmldbg_server.so
%{_qt_prefix}/plugins/qmltooling/libqmldbg_tcp.so
%{_qt_prefix}/qml/Qt/labs/folderlistmodel
%{_qt_prefix}/qml/Qt/labs/settings
%{_qt_prefix}/qml/Qt/labs/sharedimage
%{_qt_prefix}/qml/Qt/labs/qmlmodels
%{_qt_prefix}/qml/Qt/labs/wavefrontmesh

#------------------------------------------------------------------------------

%package -n %{qtquicktest}
Summary:	Qt%{api} Lib
Group:		System/Libraries

%description -n %{qtquicktest}
Qt%{api} Lib.

%files -n %{qtquicktest}
%{_qt5_libdir}/libQt5QuickTest.so.%{api}*
%{_libdir}/qt5/qml/Qt/test

#------------------------------------------------------------------------------

%package -n %{qtquicktestd}
Summary:	Devel files needed to build apps based on Qt%{api}
Group:		Development/KDE and Qt
Requires:	%{qtquicktest} = %{version}
Requires:	%{name} = %{version}

%description -n %{qtquicktestd}
Devel files needed to build apps based on Qt%{api}.

%files -n %{qtquicktestd}
%{_qt5_libdir}/libQt5QuickTest.prl
%{_qt5_libdir}/libQt5QuickTest.so
%{_qt5_libdir}/cmake/Qt5QuickTest
%{_qt5_includedir}/QtQuickTest
%exclude %{_qt5_includedir}/QtQuickTest/%{version}
%{_qt5_libdir}/pkgconfig/Qt5QuickTest.pc
%{_libdir}/metatypes/qt5quicktest_metatypes.json

#------------------------------------------------------------------------------

%package -n %{quicktest_p_d}
Summary:	Devel files needed to build apps based on Qt%{api}
Group:		Development/KDE and Qt
Requires:	%{qtquicktestd} = %{version}
Provides:	qt5-quicktest-private-devel = %{version}

%description -n %{quicktest_p_d}
Devel files needed to build apps based on Qt%{api}.

%files -n %{quicktest_p_d}
%{_qt5_includedir}/QtQuickTest/%{version}

#------------------------------------------------------------------------------

%package -n %{qtquick}
Summary:	Qt%{api} Lib
Group:		System/Libraries

%description -n %{qtquick}
Qt%{api} Lib.

%files -n %{qtquick}
%{_qt5_libdir}/libQt5Quick.so.%{api}*
%{_qt_prefix}/qml/QtQml
%dir %{_qt5_libdir}/qt5/qml
%dir %{_qt5_libdir}/qt5/qml/Qt
%dir %{_qt5_libdir}/qt5/qml/Qt/labs

#------------------------------------------------------------------------------

%package -n %{qtquickd}
Summary:	Devel files needed to build apps based on Qt%{api}
Group:		Development/KDE and Qt
Requires:	%{name} = %{version}
Requires:	%{qtquick} = %{version}

%description -n %{qtquickd}
Devel files needed to build apps based on Qt%{api}.

%files -n %{qtquickd}
%{_qt5_libdir}/libQt5Quick.prl
%{_qt5_libdir}/libQt5Quick.so
%{_qt5_libdir}/cmake/Qt5Quick
%{_qt5_includedir}/QtQuick
%{_qt5_includedir}/QtQmlDebug
%exclude %{_qt5_includedir}/QtQuick/%{version}
%{_qt5_libdir}/pkgconfig/Qt5Quick.pc
%{_qt_prefix}/mkspecs/modules/qt_lib_quick.pri
%{_qt_prefix}/mkspecs/features/qtquickcompiler.prf
#_qt5_libdir/cmake/Qt5Widgets/Qt5Widgets_AccessibleQuickFactory.cmake
%{_qt_prefix}/plugins/qmltooling/libqmldbg_messages.so
%{_qt_prefix}/plugins/qmltooling/libqmldbg_nativedebugger.so
%{_qt_prefix}/plugins/qmltooling/libqmldbg_preview.so
%{_libdir}/cmake/Qt5QuickCompiler
%{_libdir}/cmake/Qt5QmlImportScanner
%{_libdir}/metatypes/qt5quick_metatypes.json

#------------------------------------------------------------------------------

%package -n %{qtquick_p_d}
Summary:	Devel files needed to build apps based on Qt%{api}
Group:		Development/KDE and Qt
Requires:	%{qtquickd} = %{version}
Requires:	%{qtqml_p_d} = %{version}
Provides:	qt5-qtquick-private-devel = %{version}

%description -n %{qtquick_p_d}
Devel files needed to build apps based on Qt%{api}.

%files -n %{qtquick_p_d}
%{_qt5_includedir}/QtQuick/%{version}
%{_qt5_includedir}/QtQmlDebug/%{version}
%{_qt_prefix}/mkspecs/modules/qt_lib_quick_private.pri
%{_qt5_includedir}/QtPacketProtocol
%{_qt5_libdir}/libQt5PacketProtocol.a
%{_qt5_libdir}/libQt5PacketProtocol.prl
%{_qt_prefix}/mkspecs/modules/qt_lib_packetprotocol_private.pri
%{_qt5_libdir}/libQt5QmlDebug.a
%{_qt5_libdir}/libQt5QmlDebug.prl
%{_qt_prefix}/mkspecs/modules/qt_lib_qmldebug_private.pri
%{_libdir}/cmake/Qt%{api}PacketProtocol
%{_libdir}/cmake/Qt%{api}QmlDebug

#------------------------------------------------------------------------------

%package -n %{qtquickshapes}
Summary:	Qt%{api} Lib
Group:		System/Libraries

%description -n %{qtquickshapes}
Qt%{api} Lib.

%files -n %{qtquickshapes}
%{_qt5_libdir}/libQt5QuickShapes.so.%{api}*

#------------------------------------------------------------------------------

%package -n %{qtquickshapesd}
Summary:	Devel files needed to build apps based on Qt%{api}
Group:		Development/KDE and Qt
Requires:	%{name} = %{version}
Requires:	%{qtquickshapes} = %{version}

%description -n %{qtquickshapesd}
Devel files needed to build apps based on Qt%{api}.

%files -n %{qtquickshapesd}
%{_qt5_libdir}/libQt5QuickShapes.prl
%{_qt5_libdir}/libQt5QuickShapes.so
%{_qt5_includedir}/QtQuickShapes
%exclude %{_qt5_includedir}/QtQuickShapes/%{version}
%{_libdir}/cmake/Qt%{api}QuickShapes
%{_libdir}/metatypes/qt5quickshapes_metatypes.json

#------------------------------------------------------------------------------

%package -n %{qtquickshapes_p_d}
Summary:	Devel files needed to build apps based on Qt%{api}
Group:		Development/KDE and Qt
Requires:	%{qtquickshapesd} = %{version}
Requires:	%{qtqml_p_d} = %{version}
Provides:	qt5-qtquickshapes-private-devel = %{version}

%description -n %{qtquickshapes_p_d}
Devel files needed to build apps based on Qt%{api}.

%files -n %{qtquickshapes_p_d}
%{_qt5_includedir}/QtQuickShapes/%{version}
%{_qt_prefix}/mkspecs/modules/qt_lib_quickshapes_private.pri

#------------------------------------------------------------------------------

%package -n %{qtquickwidgets}
Summary:	Qt%{api} Lib
Group:		System/Libraries

%description -n %{qtquickwidgets}
Qt%{api} Lib.

%files -n %{qtquickwidgets}
%{_qt5_libdir}/libQt5QuickWidgets.so.%{api}*

#------------------------------------------------------------------------------

%package -n %{qtquickwidgetsd}
Summary:	Devel files needed to build apps based on Qt%{api}
Group:		Development/KDE and Qt
Requires:	%{name} = %{version}
Requires:	%{qtquickwidgets} = %{version}

%description -n %{qtquickwidgetsd}
Devel files needed to build apps based on Qt%{api}.

%files -n %{qtquickwidgetsd}
%{_qt5_libdir}/libQt5QuickWidgets.prl
%{_qt5_libdir}/libQt5QuickWidgets.so
%{_qt5_libdir}/cmake/Qt5QuickWidgets
%{_qt5_includedir}/QtQuickWidgets
%exclude %{_qt5_includedir}/QtQuickWidgets/%{version}
%{_qt5_libdir}/pkgconfig/Qt5QuickWidgets.pc
%{_qt_prefix}/mkspecs/modules/qt_lib_quickwidgets.pri

#------------------------------------------------------------------------------

%package -n %{qtquickwidgetsd_p_d}
Summary:	Devel files needed to build apps based on Qt%{api}
Group:		Development/KDE and Qt
Requires:	%{qtquickwidgetsd} = %{version}
Requires:	%{qtqml_p_d} = %{version}
Provides:	qt5-qtquickwidgets-private-devel = %{version}

%description -n %{qtquickwidgetsd_p_d}
Devel files needed to build apps based on Qt%{api}.

%files -n %{qtquickwidgetsd_p_d}
%{_qt5_includedir}/QtQuickWidgets/%{version}
%{_qt_prefix}/mkspecs/modules/qt_lib_quickwidgets_private.pri

#------------------------------------------------------------------------------

%package -n %{qtquickparticles}
Summary:	Qt%{api} Lib
Group:		System/Libraries

%description -n %{qtquickparticles}
Qt%{api} Lib.

%files -n %{qtquickparticles}
%{_qt5_libdir}/libQt5QuickParticles.so.%{api}*

#------------------------------------------------------------------------------

%package -n %{qtquickparticlesd}
Summary:	Devel files needed to build apps based on Qt%{api}
Group:		Development/KDE and Qt
Requires:	%{name} = %{version}
Requires:	%{qtquickparticles} = %{version}

%description -n %{qtquickparticlesd}
Devel files needed to build apps based on Qt%{api}.

%files -n %{qtquickparticlesd}
%{_qt5_libdir}/libQt5QuickParticles.prl
%{_qt5_libdir}/libQt5QuickParticles.so
%{_qt5_includedir}/QtQuickParticles
%exclude %{_qt5_includedir}/QtQuickParticles/%{version}
%{_libdir}/cmake/Qt%{api}QuickParticles
%{_libdir}/metatypes/qt5quickparticles_metatypes.json

#------------------------------------------------------------------------------

%package -n %{qtquickparticles_p_d}
Summary:	Devel files needed to build apps based on Qt%{api}
Group:		Development/KDE and Qt
Requires:	%{qtquickparticlesd} = %{version}
Provides:	qt5-qtquickparticles-private-devel = %{version}

%description -n %{qtquickparticles_p_d}
Devel files needed to build apps based on Qt%{api}.

%files -n %{qtquickparticles_p_d}
%{_qt5_includedir}/QtQuickParticles/%{version}
%{_qt_prefix}/mkspecs/modules/qt_lib_quickparticles_private.pri

#------------------------------------------------------------------------------

%package -n %{qtqml}
Summary:	Qt%{api} Lib
Group:		System/Libraries

%description -n %{qtqml}
Qt%{api} Lib.

%files -n %{qtqml}
%{_qt5_libdir}/libQt5Qml.so.%{api}*

#------------------------------------------------------------------------------

%package -n %{qtqmld}
Summary:	Devel files needed to build apps based on Qt%{api}
Group:		Development/KDE and Qt
Requires:	%{name} = %{version}
Requires:	%{qtqml} = %{version}
Requires:	pkgconfig(Qt5Core) = %{version}
Requires:	pkgconfig(Qt5Network) = %{version}
Requires:	%{qtquickd} = %{EVRD}
Requires:	rpm-provreq-qml >= 6.0.0

%description -n %{qtqmld}
Devel files needed to build apps based on Qt%{api}.

%files -n %{qtqmld}
%{_qt5_libdir}/libQt5Qml.prl
%{_qt5_libdir}/libQt5Qml.so
%{_qt5_libdir}/cmake/Qt5Qml
%{_qt_prefix}/mkspecs/modules/qt_lib_qmltest.pri
%{_qt_prefix}/mkspecs/modules/qt_lib_qml.pri
%{_qt5_libdir}/pkgconfig/Qt5Qml.pc
%{_qt5_libdir}/libQt5QmlDevTools.a
%{_qt5_includedir}/QtQml
%exclude %{_qt5_includedir}/QtQml/%{version}
%{_qt5_libdir}/libQt5QmlDevTools.prl
%{_libdir}/cmake/Qt%{api}QmlDevTools
%{_libdir}/metatypes/qt5qml_metatypes.json
%{_libdir}/qt5/mkspecs/features/qmltypes.prf
%{_libdir}/qt5/bin/qmlformat
%{_libdir}/qt5/bin/qmltyperegistrar
%{_bindir}/qmlformat
%{_bindir}/qmltyperegistrar

#------------------------------------------------------------------------------

%package -n %{qtqml_p_d}
Summary:	Devel files needed to build apps based on Qt%{api}
Group:		Development/KDE and Qt
Requires:	%{qtqmld} = %{version}
Provides:	qt5-qtqml-private-devel = %{version}
Requires:	pkgconfig(Qt5Core) = %{version}

%description -n %{qtqml_p_d}
Devel files needed to build apps based on Qt%{api}.

%files -n %{qtqml_p_d}
%{_qt5_includedir}/QtQml/%{version}
%{_qt_prefix}/mkspecs/modules/qt_lib_qml_private.pri
%{_qt_prefix}/mkspecs/modules/qt_lib_qmldevtools_private.pri
%{_qt_prefix}/mkspecs/modules/qt_lib_qmltest_private.pri

#------------------------------------------------------------------------------

%package -n %{qtqmlmodels}
Summary:	Qt%{api} QmlModels Lib
Group:		System/Libraries

%description -n %{qtqmlmodels}
Qt%{api} QmlModels Lib.

%files -n %{qtqmlmodels}
%{_qt5_libdir}/libQt5QmlModels.so.%{api}*

#------------------------------------------------------------------------------

%package -n %{qtqmlmodelsd}
Summary:	Devel files needed to build apps based on Qt%{api} QmlModels
Group:		Development/KDE and Qt
Requires:	%{name} = %{version}
Requires:	%{qtqmlmodels} = %{version}
Requires:	pkgconfig(Qt5Core) = %{version}
Requires:	pkgconfig(Qt5Network) = %{version}
Requires:	%{qtqmld} = %{EVRD}

%description -n %{qtqmlmodelsd}
Devel files needed to build apps based on Qt%{api} QmlModels.

%files -n %{qtqmlmodelsd}
%{_qt5_libdir}/libQt5QmlModels.prl
%{_qt5_libdir}/libQt5QmlModels.so
%{_qt5_libdir}/pkgconfig/Qt5QmlModels.pc
%{_qt5_includedir}/QtQmlModels*
%exclude %{_qt5_includedir}/QtQmlModels/%{version}
%{_libdir}/cmake/Qt%{api}QmlModels
%{_libdir}/qt5/mkspecs/modules/qt_lib_qmlmodels.pri
%{_libdir}/metatypes/qt5qmlmodels_metatypes.json

#------------------------------------------------------------------------------

%package -n %{qtqmlmodels_p_d}
Summary:	Devel files needed to build apps based on Qt%{api} QmlModels
Group:		Development/KDE and Qt
Requires:	%{qtqmlmodelsd} = %{version}
Provides:	qt5-qtqmlmodels-private-devel = %{version}
Requires:	pkgconfig(Qt5Core) = %{version}

%description -n %{qtqmlmodels_p_d}
Devel files needed to build apps based on Qt%{api} QmlModels.

%files -n %{qtqmlmodels_p_d}
%{_qt5_includedir}/QtQmlModels/%{version}
%{_libdir}/qt5/mkspecs/modules/qt_lib_qmlmodels_private.pri

#------------------------------------------------------------------------------

%package -n %{qtqmlworkerscript}
Summary:	Qt%{api} QmlWorkerScript Lib
Group:		System/Libraries

%description -n %{qtqmlworkerscript}
Qt%{api} Lib.

%files -n %{qtqmlworkerscript}
%{_qt5_libdir}/libQt5QmlWorkerScript.so.%{api}*

#------------------------------------------------------------------------------

%package -n %{qtqmlworkerscriptd}
Summary:	Devel files needed to build apps based on Qt%{api} QmlWorkerScript
Group:		Development/KDE and Qt
Requires:	%{name} = %{version}
Requires:	%{qtqmlworkerscript} = %{version}
Requires:	pkgconfig(Qt5Core) = %{version}
Requires:	pkgconfig(Qt5Network) = %{version}
Requires:	%{qtquickd} = %{EVRD}

%description -n %{qtqmlworkerscriptd}
Devel files needed to build apps based on Qt%{api}.

%files -n %{qtqmlworkerscriptd}
%{_qt5_libdir}/libQt5QmlWorkerScript.prl
%{_qt5_libdir}/libQt5QmlWorkerScript.so
%{_qt5_libdir}/cmake/Qt5QmlWorkerScript
%{_qt5_libdir}/pkgconfig/Qt5QmlWorkerScript.pc
%{_qt5_includedir}/QtQmlWorkerScript
%exclude %{_qt5_includedir}/QtQmlWorkerScript/%{version}
%{_libdir}/qt5/mkspecs/modules/qt_lib_qmlworkerscript.pri
%{_libdir}/metatypes/qt5qmlworkerscript_metatypes.json

#------------------------------------------------------------------------------

%package -n %{qtqmlworkerscript_p_d}
Summary:	Devel files needed to build apps based on Qt%{api} QmlWorkerScript
Group:		Development/KDE and Qt
Requires:	%{qtqmld} = %{version}
Provides:	qt5-qtqmlworkerscript-private-devel = %{version}
Requires:	pkgconfig(Qt5Core) = %{version}

%description -n %{qtqmlworkerscript_p_d}
Devel files needed to build apps based on Qt%{api} QmlWorkerScript.

%files -n %{qtqmlworkerscript_p_d}
%{_qt5_includedir}/QtQmlWorkerScript/%{version}
%{_libdir}/qt5/mkspecs/modules/qt_lib_qmlworkerscript_private.pri

#------------------------------------------------------------------------------

%package animation
Summary:	Animation support for Qt Declarative
Group:		System/Libraries

%description animation
Animation support for Qt Declarative.

%files animation
%{_libdir}/qt5/qml/Qt/labs/animation

#------------------------------------------------------------------------------
%package examples
Summary:	Examples for the use of Qt Declarative
Group:		Documentation

%description examples
Examples for the use of Qt Declarative.

%files examples
%{_qt_prefix}/examples/qml
%{_qt_prefix}/examples/qmltest
%{_qt_prefix}/examples/quick

#------------------------------------------------------------------------------

%prep
%autosetup -n %(echo %{qttarballdir}|sed -e 's,-opensource,,') -p1
%{_qt_prefix}/bin/syncqt.pl -version %{version}

# FIXME at some point we need to determine if this is needed because
# of a Qt bug or because of a clang bug... In the mean time, this
# workaround keeps things going
find . -name "*.cpp" |while read r; do
    if grep -E 'qml(Warning|Info|Context|Engine|Execute)' $r; then
	sed -i -e '/QT_BEGIN_NAMESPACE/ausing namespace QtQml;' $r
    fi
done
sed -i -e 's,qmlWarning,QtQml::qmlWarning,g' src/particles/qquickspritegoal_p.h

%build
%qmake_qt5

#------------------------------------------------------------------------------
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

## .prl/.la file love
# nuke .prl reference(s) to %%buildroot, excessive (.la-like) libs
cd %{buildroot}%{_qt5_libdir}
for prl_file in libQt5*.prl ; do
  sed -i \
    -e "/^QMAKE_PRL_BUILD_DIR/d" \
    ${prl_file}
  if [ -f "$(basename ${prl_file} .prl).so" ]; then
    rm -fv "$(basename ${prl_file} .prl).la"
  else
    sed -i \
       -e "/^QMAKE_PRL_LIBS/d" \
       $(basename ${prl_file} .prl).la
  fi
done
cd -

# .la and .a files, die, die, die.
rm -f %{buildroot}%{_qt5_libdir}/lib*.la

mkdir -p %{buildroot}%{_bindir}
ln -s ../%{_lib}/qt5/bin/qmlformat %{buildroot}%{_bindir}/qmlformat
ln -s ../%{_lib}/qt5/bin/qmltyperegistrar %{buildroot}%{_bindir}/qmltyperegistrar
