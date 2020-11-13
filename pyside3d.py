import sys
from PyQt5 import QtWidgets, QtCore, QtGui, Qt3DExtras, Qt3DCore, Qt3DInput, Qt3DRender
from PyQt5.QtGui import QColor


class SceneModifier(QtCore.QObject):
    def __init__(self, root_entity=None):
        super().__init__()
        self.m_rootEntity = root_entity

        self.m_torus = Qt3DExtras.QTorusMesh(
            radius=1.0, minorRadius=0.4, rings=100, slices=20
        )

        self.torusTransform = Qt3DCore.QTransform(
            scale=2.0,
            rotation=QtGui.QQuaternion.fromAxisAndAngle(
                QtGui.QVector3D(0.0, 1.0, 0.0), 25.0
            ),
            translation=QtGui.QVector3D(5.0, 4.0, 0.0),
        )

        self.torusMaterial = Qt3DExtras.QPhongMaterial(diffuse=QtGui.QColor("#beb32b"))

        self.m_torusEntity = Qt3DCore.QEntity(self.m_rootEntity)
        self.m_torusEntity.addComponent(self.m_torus)
        self.m_torusEntity.addComponent(self.torusMaterial)
        self.m_torusEntity.addComponent(self.torusTransform)

        self.cone = Qt3DExtras.QConeMesh(
            topRadius=0.5, bottomRadius=1, length=3, rings=50, slices=20
        )

        self.coneTransform = Qt3DCore.QTransform(
            scale=1.5,
            rotation=QtGui.QQuaternion.fromAxisAndAngle(
                QtGui.QVector3D(1.0, 4.0, -1.5), 45.0
            ),
            translation=QtGui.QVector3D(0.0, 4.0, -1.5),
        )

        self.coneMaterial = Qt3DExtras.QPhongMaterial(diffuse=QtGui.QColor("#928327"))

        self.m_coneEntity = Qt3DCore.QEntity(self.m_rootEntity)
        self.m_coneEntity.addComponent(self.cone)
        self.m_coneEntity.addComponent(self.coneMaterial)
        self.m_coneEntity.addComponent(self.coneTransform)

        self.cylinder = Qt3DExtras.QCylinderMesh(
            radius=1, length=3, rings=100, slices=20
        )

        self.cylinderTransform = Qt3DCore.QTransform(
            scale=1.5,
            rotation=QtGui.QQuaternion.fromAxisAndAngle(
                QtGui.QVector3D(1.0, 0.0, 0.0), 45.0
            ),
            translation=QtGui.QVector3D(-5.0, 4.0, -1.5),
        )

        self.cylinderMaterial = Qt3DExtras.QPhongMaterial(
            diffuse=QtGui.QColor("#928327")
        )

        self.m_cylinderEntity = Qt3DCore.QEntity(self.m_rootEntity)
        self.m_cylinderEntity.addComponent(self.cylinder)
        self.m_cylinderEntity.addComponent(self.cylinderMaterial)
        self.m_cylinderEntity.addComponent(self.cylinderTransform)

        self.cuboid = Qt3DExtras.QCuboidMesh()

        self.cuboidTransform = Qt3DCore.QTransform(
            scale=4.0, translation=QtGui.QVector3D(5.0, -4.0, 0.0),
        )

        self.cuboidMaterial = Qt3DExtras.QPhongMaterial(diffuse=QtGui.QColor("#665423"))

        self.m_cuboidEntity = Qt3DCore.QEntity(self.m_rootEntity)
        self.m_cuboidEntity.addComponent(self.cuboid)
        self.m_cuboidEntity.addComponent(self.cuboidMaterial)
        self.m_cuboidEntity.addComponent(self.cuboidTransform)

        self.planeMesh = Qt3DExtras.QPlaneMesh(width=2, height=2)

        self.planeTransform = Qt3DCore.QTransform(
            scale=1.3,
            rotation=QtGui.QQuaternion.fromAxisAndAngle(
                QtGui.QVector3D(1.0, 0.0, 0.0), 45.0
            ),
            translation=QtGui.QVector3D(0.0, -4.0, 0.0),
        )

        self.planeMaterial = Qt3DExtras.QPhongMaterial(diffuse=QtGui.QColor("#a69929"))

        self.m_planeEntity = Qt3DCore.QEntity(self.m_rootEntity)
        self.m_planeEntity.addComponent(self.planeMesh)
        self.m_planeEntity.addComponent(self.planeMaterial)
        self.m_planeEntity.addComponent(self.planeTransform)

        self.sphereMesh = Qt3DExtras.QSphereMesh(rings=20, slices=20, radius=2)

        self.sphereTransform = Qt3DCore.QTransform(
            scale=1.3, translation=QtGui.QVector3D(-5.0, -4.0, 0.0),
        )

        self.sphereMaterial = Qt3DExtras.QPhongMaterial(diffuse=QtGui.QColor("#a69929"))

        self.m_sphereEntity = Qt3DCore.QEntity(self.m_rootEntity)
        self.m_sphereEntity.addComponent(self.sphereMesh)
        self.m_sphereEntity.addComponent(self.sphereMaterial)
        self.m_sphereEntity.addComponent(self.sphereTransform)

    def enableTorus(self, enabled):
        self.m_torusEntity.setEnabled(enabled)

    def enableCone(self, enabled):
        self.m_coneEntity.setEnabled(enabled)

    def enableCylinder(self, enabled):
        self.m_cylinderEntity.setEnabled(enabled)

    def enableCuboid(self, enabled):
        self.m_cuboidEntity.setEnabled(enabled)

    def enablePlane(self, enabled):
        self.m_planeEntity.setEnabled(enabled)

    def enableSphere(self, enabled):
        self.m_sphereEntity.setEnabled(enabled)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    view = Qt3DExtras.Qt3DWindow()
    view.defaultFrameGraph().setClearColor(QtGui.QColor("#4d4d4f"))
    container = QtWidgets.QWidget.createWindowContainer(view)
    screenSize = view.screen().size()
    container.setMinimumSize(QtCore.QSize(200, 100))
    container.setMaximumSize(screenSize)

    widget = QtWidgets.QWidget()
    hLayout = QtWidgets.QHBoxLayout(widget)
    vLayout = QtWidgets.QVBoxLayout()
    vLayout.setAlignment(QtCore.Qt.AlignTop)
    hLayout.addWidget(container, 1)
    hLayout.addLayout(vLayout)

    widget.setWindowTitle("Basic shapes")

    input_ = Qt3DInput.QInputAspect()
    view.registerAspect(input_)

    rootEntity = Qt3DCore.QEntity()

    cameraEntity = view.camera()

    cameraEntity.lens().setPerspectiveProjection(45.0, 16.0 / 9.0, 0.1, 1000.0)
    cameraEntity.setPosition(QtGui.QVector3D(0, 0, 20.0))
    cameraEntity.setUpVector(QtGui.QVector3D(0, 1, 0))
    cameraEntity.setViewCenter(QtGui.QVector3D(0, 0, 0))

    lightEntity = Qt3DCore.QEntity(rootEntity)
    light = Qt3DRender.QPointLight(lightEntity)
    light.setColor(QColor("white"))
    light.setIntensity(1)
    lightEntity.addComponent(light)

    lightTransform = Qt3DCore.QTransform(lightEntity)
    lightTransform.setTranslation(cameraEntity.position())
    lightEntity.addComponent(lightTransform)

    camController = Qt3DExtras.QFirstPersonCameraController(rootEntity)
    camController.setCamera(cameraEntity)

    modifier = SceneModifier(rootEntity)

    view.setRootEntity(rootEntity)

    info = QtWidgets.QCommandLinkButton()
    info.setText("Qt3D ready-made meshes")
    info.setDescription(
        "Qt3D provides several ready-made meshes, like torus, cylinder, cone, cube, plane and sphere."
    )
    info.setIconSize(QtCore.QSize(0, 0))

    torusCB = QtWidgets.QCheckBox(widget)
    torusCB.setChecked(True)
    torusCB.setText("Torus")

    coneCB = QtWidgets.QCheckBox(widget)
    coneCB.setChecked(True)
    coneCB.setText("Cone")

    cylinderCB = QtWidgets.QCheckBox(widget)
    cylinderCB.setChecked(True)
    cylinderCB.setText("Cylinder")

    cuboidCB = QtWidgets.QCheckBox(widget)
    cuboidCB.setChecked(True)
    cuboidCB.setText("Cuboid")

    planeCB = QtWidgets.QCheckBox(widget)
    planeCB.setChecked(True)
    planeCB.setText("Plane")

    sphereCB = QtWidgets.QCheckBox(widget)
    sphereCB.setChecked(True)
    sphereCB.setText("Sphere")

    vLayout.addWidget(info)
    vLayout.addWidget(torusCB)
    vLayout.addWidget(coneCB)
    vLayout.addWidget(cylinderCB)
    vLayout.addWidget(cuboidCB)
    vLayout.addWidget(planeCB)
    vLayout.addWidget(sphereCB)

    torusCB.stateChanged.connect(modifier.enableTorus)
    coneCB.stateChanged.connect(modifier.enableCone)
    cylinderCB.stateChanged.connect(modifier.enableCylinder)
    cuboidCB.stateChanged.connect(modifier.enableCuboid)
    planeCB.stateChanged.connect(modifier.enablePlane)
    sphereCB.stateChanged.connect(modifier.enableSphere)

    torusCB.setChecked(True)
    coneCB.setChecked(True)
    cylinderCB.setChecked(True)
    cuboidCB.setChecked(True)
    planeCB.setChecked(True)
    sphereCB.setChecked(True)

    widget.show()
    widget.resize(1200, 800)

    sys.exit(app.exec_())
