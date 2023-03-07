# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.richtext

###########################################################################
## Class VentanaPrincipal
###########################################################################

class VentanaPrincipal ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Organizador v1.0", pos = wx.DefaultPosition, size = wx.Size( 1061,582 ), style = wx.DEFAULT_FRAME_STYLE|wx.BORDER_SUNKEN|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 18, 138, 61 ) )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticline5 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		self.m_staticline5.SetBackgroundColour( wx.Colour( 229, 236, 235 ) )

		bSizer3.Add( self.m_staticline5, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText_Kanban = wx.StaticText( self, wx.ID_ANY, u"TABLERO KANBAN", wx.DefaultPosition, wx.DefaultSize, 0|wx.BORDER_NONE|wx.TRANSPARENT_WINDOW )
		self.m_staticText_Kanban.Wrap( -1 )

		self.m_staticText_Kanban.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Abyssinica SIL" ) )
		self.m_staticText_Kanban.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_staticText_Kanban.SetBackgroundColour( wx.Colour( 18, 138, 61 ) )

		bSizer15.Add( self.m_staticText_Kanban, 1, wx.ALIGN_CENTER|wx.ALL, 5 )

		bSizer17 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_textCtrl_Proyecto = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.BORDER_RAISED|wx.BORDER_SUNKEN )
		self.m_textCtrl_Proyecto.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Sawasdee" ) )
		self.m_textCtrl_Proyecto.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_textCtrl_Proyecto.SetBackgroundColour( wx.Colour( 18, 138, 61 ) )
		self.m_textCtrl_Proyecto.SetToolTip( u"Nombre del proyecto" )

		bSizer17.Add( self.m_textCtrl_Proyecto, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer15.Add( bSizer17, 1, 0, 5 )


		bSizer3.Add( bSizer15, 1, wx.EXPAND, 5 )

		self.m_staticline6 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		self.m_staticline6.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer3.Add( self.m_staticline6, 0, wx.EXPAND |wx.ALL, 5 )


		bSizer11.Add( bSizer3, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		wSizer1 = wx.WrapSizer( wx.VERTICAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_bmToggleBtn_NuevoProyecto = wx.BitmapToggleButton( self, wx.ID_ANY, wx.Bitmap( u"recursos/nuevo_tablero.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )

		self.m_bmToggleBtn_NuevoProyecto.SetBitmap( wx.Bitmap( u"recursos/nuevo_tablero.png", wx.BITMAP_TYPE_ANY ) )
		self.m_bmToggleBtn_NuevoProyecto.SetToolTip( u"Nuevo tablero" )

		wSizer1.Add( self.m_bmToggleBtn_NuevoProyecto, 0, wx.ALL, 5 )

		self.m_bmToggleBtn_Editar = wx.BitmapToggleButton( self, wx.ID_ANY, wx.Bitmap( u"recursos/editar_etiqueta.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )

		self.m_bmToggleBtn_Editar.SetBitmap( wx.Bitmap( u"recursos/editar_etiqueta.png", wx.BITMAP_TYPE_ANY ) )
		self.m_bmToggleBtn_Editar.SetToolTip( u"Editar tablero" )

		wSizer1.Add( self.m_bmToggleBtn_Editar, 0, wx.ALL, 5 )

		self.m_bmToggleBtn_Mover = wx.BitmapToggleButton( self, wx.ID_ANY, wx.Bitmap( u"recursos/mover_etiqueta.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )

		self.m_bmToggleBtn_Mover.SetBitmap( wx.Bitmap( u"recursos/mover_etiqueta.png", wx.BITMAP_TYPE_ANY ) )
		self.m_bmToggleBtn_Mover.SetToolTip( u"Mover etiquetas" )

		wSizer1.Add( self.m_bmToggleBtn_Mover, 0, wx.ALL, 5 )

		self.m_bpButton_Cargar = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton_Cargar.SetBitmap( wx.Bitmap( u"recursos/cargar_tablero.png", wx.BITMAP_TYPE_ANY ) )
		self.m_bpButton_Cargar.SetToolTip( u"Cargar tablero" )

		wSizer1.Add( self.m_bpButton_Cargar, 0, wx.ALL, 5 )

		self.m_bpButton_Salvar = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton_Salvar.SetBitmap( wx.Bitmap( u"recursos/guardar_fichero.png", wx.BITMAP_TYPE_ANY ) )
		self.m_bpButton_Salvar.SetToolTip( u"Salvar tablero" )

		wSizer1.Add( self.m_bpButton_Salvar, 0, wx.ALL, 5 )

		self.m_bpButton_Salir = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton_Salir.SetBitmap( wx.Bitmap( u"recursos/salida_app.png", wx.BITMAP_TYPE_ANY ) )
		self.m_bpButton_Salir.SetToolTip( u"Salir de la aplicación" )

		wSizer1.Add( self.m_bpButton_Salir, 0, wx.ALL, 5 )

		self.m_bpButton_Ayuda = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton_Ayuda.SetBitmap( wx.Bitmap( u"recursos/informacion.png", wx.BITMAP_TYPE_ANY ) )
		self.m_bpButton_Ayuda.SetToolTip( u"Ayuda" )

		wSizer1.Add( self.m_bpButton_Ayuda, 0, wx.ALL, 5 )

		self.m_bpButton_AcercaDe = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton_AcercaDe.SetBitmap( wx.Bitmap( u"recursos/acercade.png", wx.BITMAP_TYPE_ANY ) )
		self.m_bpButton_AcercaDe.SetToolTip( u"Acerca de" )

		wSizer1.Add( self.m_bpButton_AcercaDe, 0, wx.ALL, 5 )


		bSizer4.Add( wSizer1, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer21 = wx.BoxSizer( wx.VERTICAL )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel_izq_aux = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel_izq_aux.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer111 = wx.BoxSizer( wx.VERTICAL )

		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText2 = wx.StaticText( self.m_panel_izq_aux, wx.ID_ANY, u"PENDIENTE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		self.m_staticText2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Sans" ) )
		self.m_staticText2.SetForegroundColour( wx.Colour( 18, 138, 61 ) )
		self.m_staticText2.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer12.Add( self.m_staticText2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_bpButton_CrearEtiquetaIzq = wx.BitmapButton( self.m_panel_izq_aux, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton_CrearEtiquetaIzq.SetBitmap( wx.Bitmap( u"recursos/crear_etiqueta.png", wx.BITMAP_TYPE_ANY ) )
		self.m_bpButton_CrearEtiquetaIzq.SetToolTip( u"Crear etiqueta" )

		bSizer12.Add( self.m_bpButton_CrearEtiquetaIzq, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_bpButton_BorrarEtiquetaIzq = wx.BitmapButton( self.m_panel_izq_aux, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton_BorrarEtiquetaIzq.SetBitmap( wx.Bitmap( u"recursos/eliminar_etiqueta.png", wx.BITMAP_TYPE_ANY ) )
		self.m_bpButton_BorrarEtiquetaIzq.SetToolTip( u"Borrar etiqueta" )

		bSizer12.Add( self.m_bpButton_BorrarEtiquetaIzq, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer111.Add( bSizer12, 0, wx.EXPAND, 5 )

		self.m_panel_izq = wx.Panel( self.m_panel_izq_aux, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE|wx.TAB_TRAVERSAL )
		self.m_panel_izq.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_panel_izq.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer111.Add( self.m_panel_izq, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel_izq_aux.SetSizer( bSizer111 )
		self.m_panel_izq_aux.Layout()
		bSizer111.Fit( self.m_panel_izq_aux )
		bSizer10.Add( self.m_panel_izq_aux, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer9.Add( bSizer10, 1, wx.EXPAND, 5 )


		bSizer5.Add( bSizer9, 1, wx.EXPAND, 5 )

		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		self.m_staticline1.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer5.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer91 = wx.BoxSizer( wx.VERTICAL )

		bSizer101 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel_central_aux = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel_central_aux.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer1111 = wx.BoxSizer( wx.VERTICAL )

		bSizer121 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText21 = wx.StaticText( self.m_panel_central_aux, wx.ID_ANY, u"EN PROGRESO", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		self.m_staticText21.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Sans" ) )
		self.m_staticText21.SetForegroundColour( wx.Colour( 18, 138, 61 ) )
		self.m_staticText21.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer121.Add( self.m_staticText21, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_bpButton_CrearEtiquetaCentral = wx.BitmapButton( self.m_panel_central_aux, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton_CrearEtiquetaCentral.SetBitmap( wx.Bitmap( u"recursos/crear_etiqueta.png", wx.BITMAP_TYPE_ANY ) )
		self.m_bpButton_CrearEtiquetaCentral.SetToolTip( u"Crear etiqueta" )

		bSizer121.Add( self.m_bpButton_CrearEtiquetaCentral, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_bpButton_BorrarEtiquetaCentral = wx.BitmapButton( self.m_panel_central_aux, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton_BorrarEtiquetaCentral.SetBitmap( wx.Bitmap( u"recursos/eliminar_etiqueta.png", wx.BITMAP_TYPE_ANY ) )
		self.m_bpButton_BorrarEtiquetaCentral.SetToolTip( u"Borrar etiqueta" )

		bSizer121.Add( self.m_bpButton_BorrarEtiquetaCentral, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer1111.Add( bSizer121, 0, wx.EXPAND, 5 )

		self.m_panel_central = wx.Panel( self.m_panel_central_aux, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE|wx.TAB_TRAVERSAL )
		self.m_panel_central.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_panel_central.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer1111.Add( self.m_panel_central, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel_central_aux.SetSizer( bSizer1111 )
		self.m_panel_central_aux.Layout()
		bSizer1111.Fit( self.m_panel_central_aux )
		bSizer101.Add( self.m_panel_central_aux, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer91.Add( bSizer101, 1, wx.EXPAND, 5 )


		bSizer5.Add( bSizer91, 1, wx.EXPAND, 5 )

		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		self.m_staticline2.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer5.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer92 = wx.BoxSizer( wx.VERTICAL )

		bSizer102 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel_der_aux = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel_der_aux.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer1112 = wx.BoxSizer( wx.VERTICAL )

		bSizer122 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText22 = wx.StaticText( self.m_panel_der_aux, wx.ID_ANY, u"TERMINADO", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		self.m_staticText22.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Sans" ) )
		self.m_staticText22.SetForegroundColour( wx.Colour( 18, 138, 61 ) )
		self.m_staticText22.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer122.Add( self.m_staticText22, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_bpButton_CrearEtiquetaDer = wx.BitmapButton( self.m_panel_der_aux, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton_CrearEtiquetaDer.SetBitmap( wx.Bitmap( u"recursos/crear_etiqueta.png", wx.BITMAP_TYPE_ANY ) )
		self.m_bpButton_CrearEtiquetaDer.SetToolTip( u"Crear etiqueta" )

		bSizer122.Add( self.m_bpButton_CrearEtiquetaDer, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_bpButton_BorrarEtiquetaDer = wx.BitmapButton( self.m_panel_der_aux, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton_BorrarEtiquetaDer.SetBitmap( wx.Bitmap( u"recursos/eliminar_etiqueta.png", wx.BITMAP_TYPE_ANY ) )
		self.m_bpButton_BorrarEtiquetaDer.SetToolTip( u"Borrar etiqueta" )

		bSizer122.Add( self.m_bpButton_BorrarEtiquetaDer, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer1112.Add( bSizer122, 0, wx.EXPAND, 5 )

		self.m_panel_der = wx.Panel( self.m_panel_der_aux, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE|wx.TAB_TRAVERSAL )
		self.m_panel_der.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_panel_der.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer1112.Add( self.m_panel_der, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel_der_aux.SetSizer( bSizer1112 )
		self.m_panel_der_aux.Layout()
		bSizer1112.Fit( self.m_panel_der_aux )
		bSizer102.Add( self.m_panel_der_aux, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer92.Add( bSizer102, 1, wx.EXPAND, 5 )


		bSizer5.Add( bSizer92, 1, wx.EXPAND, 5 )


		bSizer21.Add( bSizer5, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer4.Add( bSizer21, 1, wx.EXPAND, 5 )


		bSizer11.Add( bSizer4, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer11 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_bmToggleBtn_NuevoProyecto.Bind( wx.EVT_TOGGLEBUTTON, self.OnNuevoProyecto )
		self.m_bmToggleBtn_Editar.Bind( wx.EVT_TOGGLEBUTTON, self.OnEditar )
		self.m_bmToggleBtn_Mover.Bind( wx.EVT_TOGGLEBUTTON, self.OnMover )
		self.m_bpButton_Cargar.Bind( wx.EVT_BUTTON, self.OnCargarTablero )
		self.m_bpButton_Salvar.Bind( wx.EVT_BUTTON, self.OnSalvarTablero )
		self.m_bpButton_Salir.Bind( wx.EVT_BUTTON, self.OnSalirApp )
		self.m_bpButton_Ayuda.Bind( wx.EVT_BUTTON, self.OnAyuda )
		self.m_bpButton_AcercaDe.Bind( wx.EVT_BUTTON, self.OnAcercaDe )
		self.m_bpButton_CrearEtiquetaIzq.Bind( wx.EVT_BUTTON, self.OnCrearEtiquetaIzq )
		self.m_bpButton_BorrarEtiquetaIzq.Bind( wx.EVT_BUTTON, self.OnborrarEtiquetaIzq )
		self.m_bpButton_CrearEtiquetaCentral.Bind( wx.EVT_BUTTON, self.OnCrearEtiquetaCentral )
		self.m_bpButton_BorrarEtiquetaCentral.Bind( wx.EVT_BUTTON, self.OnborrarEtiquetaCentral )
		self.m_bpButton_CrearEtiquetaDer.Bind( wx.EVT_BUTTON, self.OnCrearEtiquetaDer )
		self.m_bpButton_BorrarEtiquetaDer.Bind( wx.EVT_BUTTON, self.OnborrarEtiquetaDer )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnNuevoProyecto( self, event ):
		event.Skip()

	def OnEditar( self, event ):
		event.Skip()

	def OnMover( self, event ):
		event.Skip()

	def OnCargarTablero( self, event ):
		event.Skip()

	def OnSalvarTablero( self, event ):
		event.Skip()

	def OnSalirApp( self, event ):
		event.Skip()

	def OnAyuda( self, event ):
		event.Skip()

	def OnAcercaDe( self, event ):
		event.Skip()

	def OnCrearEtiquetaIzq( self, event ):
		event.Skip()

	def OnborrarEtiquetaIzq( self, event ):
		event.Skip()

	def OnCrearEtiquetaCentral( self, event ):
		event.Skip()

	def OnborrarEtiquetaCentral( self, event ):
		event.Skip()

	def OnCrearEtiquetaDer( self, event ):
		event.Skip()

	def OnborrarEtiquetaDer( self, event ):
		event.Skip()


###########################################################################
## Class MyPanel1
###########################################################################

class MyPanel1 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.m_richText_Ayuda = wx.richtext.RichTextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		bSizer6.Add( self.m_richText_Ayuda, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer6 )
		self.Layout()

	def __del__( self ):
		pass


