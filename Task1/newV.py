import sys
from PyQt5 import QtGui, QtGui
import numpy as np
import pyqtgraph as pg
region = pg.LinearRegionItem()
minX=0
maxX=0
vb=[]
data1=0
data2=0
dataPosX=0
vLine=pg.InfiniteLine(angle=90,movable=False)
hLine=pg.InfiniteLine(angle=0,movable=False)
Colors_Set = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),(44, 160, 44), (152, 223, 138)]
majors = ["X","Y"]
pg.setConfigOption("background","w")
class pyshine_plot(QtGui.QWidget):
	def __init__(self):
		global dataPosX
		super(pyshine_plot,self).__init__()
		self.amplitude=10
		self.init_ui()
		self.t = 0
		self.qt_connections()
		self.num_of_curves=2 
		plotCurveIds = ["%d" % x for x in np.arange(self.num_of_curves)]
		curvePointsIds = ["%d" % x for x in np.arange(self.num_of_curves)]
		textIds = ["%d" % x for x in np.arange(self.num_of_curves)]
		arrowIds = ["%d" % x for x in np.arange(self.num_of_curves)]
		dataIds = ["%d" % x for x in np.arange(self.num_of_curves)]
		self.plotcurves = plotCurveIds
		self.curvePoints = curvePointsIds
		self.texts = textIds
		self.arrows = arrowIds
		self.datas = dataIds
		for k in range (self.num_of_curves):
			 self.plotcurves[k] = pg.PlotCurveItem()
		
		self.updateplot()
		
		
		for k in range (self.num_of_curves):
			self.plotwidget.addItem(self.plotcurves[k])
			self.curvePoints[k] = pg.CurvePoint(self.plotcurves[k])
			self.plotwidget.addItem(self.curvePoints[k])
			self.texts[k] = pg.TextItem(str(k),color=Colors_Set[k+2],anchor=(0.5,-1.0))
			# Here we require setParent on the TextItem
			self.texts[k].setParentItem(self.curvePoints[k])
			self.arrows[k] = pg.ArrowItem(angle=60,pen=Colors_Set[k+2],brush=Colors_Set[k])
			self.arrows[k].setParentItem(self.curvePoints[k])
		
		
		
		self.proxy = pg.SignalProxy (self.plotwidget.scene().sigMouseMoved,rateLimit = 60, slot=self.mouseMoved)
		self.timer = pg.QtCore.QTimer()
		self.timer.timeout.connect(self.moveplot)
		self.timer.start(1000)
		
	
	def init_ui(self):
		global region
		global minX
		global maxX
		global vLine
		global hLine
		global vb
		self.setWindowTitle("PyShine")
		self.label = pg.LabelItem(justify="left")
		hbox = QtGui.QVBoxLayout()
		
		self.setLayout(hbox)
		self.plotwidget = pg.PlotWidget()
		self.plotwidget.addItem(vLine,ignoreBounds=True)
		self.vb = self.plotwidget.plotItem.vb
		self.plotwidget.addItem(self.label)
		hbox.addWidget(self.plotwidget)
		self.increasebutton = QtGui.QPushButton("Increase Amplitude")
		self.decreasebutton = QtGui.QPushButton("Decrease Amplitude")
		
		
		hbox.addWidget(self.increasebutton)
		hbox.addWidget(self.decreasebutton)
		self.show()
	
	
	def mouseMoved(self,evt): 
		global hLine
		global vLine
		global data1
		global data2
		global dataPosX
		pos = evt[0] 
		
		if self.plotwidget.sceneBoundingRect().contains(pos):
			mousePoint = self.vb.mapSceneToView(pos)
			index = int(mousePoint.x())
			if index >=0 and index < len(self.datas[0]):
				dataPosX = mousePoint.x()
				
				
				for m in range (self.num_of_curves):
					self.curvePoints[m].setPos(float(index)/(len(self.datas[m])-1))
					T = majors[m] # Get the respective text string of the Legend
					self.texts[m].setText("[%0.1f,%0.1f]:"%(dataPosX,self.datas[m][index])+str(T))
			
			vLine.setPos(mousePoint.x())
			hLine.setPos(mousePoint.y())
	

	def qt_connections(self):
		self.increasebutton.clicked.connect(self.on_increasebutton_clicked)
		self.decreasebutton.clicked.connect(self.on_decreasebutton_clicked)
		
	
	def moveplot(self):
		self.updateplot() # Rather we can call the function
		
	
	def updateplot(self):
		global data1
		global data2
		
		
		self.datas[0] = self.amplitude*np.sin(np.linspace(-2*np.pi,2*np.pi,1000)+self.t)
		self.datas[1] = self.amplitude*np.cos(np.linspace(0,2*np.pi,1000)+self.t) 
		for j in range(self.num_of_curves):
			pen = pg.mkPen(color=Colors_Set[j+2],width=5)
			
			self.plotcurves[j].setData(self.datas[j],pen=pen,clickable=True)
			
	
	
	def on_increasebutton_clicked (self):
		self.amplitude+=1
		self.updateplot()
		
	def on_decreasebutton_clicked (self):
		self.amplitude-=1
		self.updateplot()



def main():
	import sys
	app = QtGui.QApplication(sys.argv)
	app.setApplicationName("Sinwave")
	ex = pyshine_plot()
	if (sys.flags.interactive!=1)or not hasattr(QtCore,"PYQT_VERSION"):
		sys.exit(app.exec_())
if __name__ == "__main__":
	main()
	
