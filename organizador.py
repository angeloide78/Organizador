import wx
import wx.adv
import wx.lib.scrolledpanel as scrolled
from wx.lib.wordwrap import wordwrap
from os.path import exists as f_exists
import json
import platform

from OrganizadorVista import VentanaPrincipal

class Seleccionar(wx.Dialog):
  def __init__(self, parent, titulo="Lista de elementos", datos=[]):
    wx.Dialog.__init__(self, parent, title=titulo)
    
    panel = wx.Panel(self)
    sizer = wx.BoxSizer(wx.VERTICAL)
    self.lista = wx.ListCtrl(panel, style=wx.LC_REPORT)
    self.lista.InsertColumn(0, "Proyectos Kanban disponibles")
    
    for i, elemento in enumerate(datos):
      self.lista.InsertItem(i, elemento)
    
    self.lista.SetColumnWidth(0, self.GetSize()[0])
    sizer.Add(self.lista, 1, wx.EXPAND|wx.ALL, 10)
    button = wx.Button(panel, label="Seleccionar")
    self.Bind(wx.EVT_BUTTON, self.seleccionar, button)
    
    sizer.Add(button, 0, wx.ALL|wx.CENTER, 10)
    panel.SetSizer(sizer)
    self.elemento_seleccionado = None  
    
    # Le damos el formato al diálogo.
    self.SetBackgroundColour(wx.Colour(18, 138, 61))
    self.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, \
                         wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, underline=False, faceName='Arial'))
    self.SetForegroundColour(wx.WHITE)
  
    self.lista.SetBackgroundColour(wx.Colour(18, 138, 61))
    self.lista.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, \
                               wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, underline=False, faceName='Arial'))
    self.lista.SetForegroundColour(wx.WHITE)
    
  def seleccionar(self, event):
    seleccion = self.lista.GetFirstSelected()
    if seleccion != -1:
      self.elemento_seleccionado = self.lista.GetItemText(seleccion)
      self.EndModal(wx.ID_OK)
      
class PanelConScroll(scrolled.ScrolledPanel):
  def __init__(self, parent):
    scrolled.ScrolledPanel.__init__(self, parent, style=wx.TAB_TRAVERSAL)
    
    # Creamos boxsizer para añadir elementos.
    self.boxsizer = wx.BoxSizer(wx.VERTICAL) 
    self.SetSizer(self.boxsizer)
    self.Layout()
   
class Ventana(VentanaPrincipal):

  def __init__(self, parent):
    VentanaPrincipal.__init__(self, parent)
    
    self.color_en_edicion = wx.Colour(0,18,248)
    
    self.ultimo_objeto = None
    self.origen_objeto = None
  
    # Por defecto todo desactivado.
    self.__activar_botones(False)
    
    # Panel izquierdo
    self.m_panel_izqScroll = self.__crear_paneles(self.m_panel_izq)

    # Panel central
    self.m_panel_centralScroll = self.__crear_paneles(self.m_panel_central)
    
    # Panel derecho
    self.m_panel_derScroll = self.__crear_paneles(self.m_panel_der)
  
  # ###################################################
  #  Manejadores de eventos de botones de la aplicación
  # ###################################################
  
  def OnAcercaDe( self, event ):
    licencia = '''
    Organizador v1.0

Copyright (C) 2023 Ángel Luis Garcia Garcia

Este programa es software libre; puede redistribuirlo y/o modificarlo bajo los términos de la Licencia Pública General de GNU según es publicada por la Free Software Foundation, ya sea la versión 2 de la Licencia, o (a su elección) cualquier versión posterior.

Este programa se distribuye con la esperanza de que sea útil, pero SIN NINGUNA GARANTÍA; ni siquiera la garantía implícita MERCANTIL o de APTITUD PARA UN PROPÓSITO DADO. Consulte los detalles de la Licencia Pública General de GNU para obtener una información más detallada.

Debería haber recibido una copia de la Licencia Pública General de GNU junto con este programa; de lo contrario, escriba a la Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, EE. UU.
    '''
    # First we create and fill the info object
    info = wx.adv.AboutDialogInfo()
    info.Name = "Organizador"
    info.Version = "1.0"
    info.Copyright = "Copyright (C) 2023 Ángel Luis Garcia Garcia"
    info.Description = wordwrap(
      "Un organizador Kanban escrito en Python y wxPython."
      "\nContiene 3 paneles fijos, Pendientes, En Progreso y Terminado."
      "\nSe pueden crear proyectos y guardarlos en disco, en formato json."
      "\nLas etiquetas pueden moverse por teclado, usando flechas y mediante"
      " el ratón, manteniendo pulsada previamente la tecla Control."
      "\n\nSe libre de modificar el código, mejóralo y aprende."
      "\n\n   Nos vemos!!",
              350, wx.ClientDC(self))
    info.WebSite = ("https://elviajedelnavegante.blogspot.es", "El viaje del Nagevante")
    info.Developers = [ "Ángel \"angeloide\" García"]
  
    info.License = wordwrap(licencia, 500, wx.ClientDC(self))
  
    # Then we call wx.AboutBox giving it that info object
    wx.adv.AboutBox(info)
    
  def OnNuevoProyecto( self, event ):
    
    # Si ya hay un proyecto en edición, se informa.
    seguir = True
    nombre_proyecto = self.m_textCtrl_Proyecto.GetValue()
    if len(nombre_proyecto.strip()) != 0:
      msg = "Hay un proyecto en edición.\nSi continúas perderás las modificaciones.\n¿Continuar?"
      ret = wx.MessageBox(msg, "Atención",wx.OK|wx.CANCEL|wx.ICON_EXCLAMATION)
      if ret != wx.OK: seguir = False 
    
    if seguir:
      # Pedir nombre de proyecto.
      dialogo = wx.TextEntryDialog(None, "Nombre del proyecto", "Crear tablero", \
                                   style=wx.OK|wx.CANCEL|wx.ICON_QUESTION)
      ret = dialogo.ShowModal()
      if ret == wx.ID_OK and len(dialogo.GetValue().strip()) > 0:
        # Se incluye nombre de proyecto.
        self.m_textCtrl_Proyecto.SetValue(dialogo.GetValue().strip().upper())
        # Se limpian los tableros.
        self.__limpiar_tableros()
        # Se activan botones.
        self.__activar_botones()
     
  def OnSalirApp( self, event ):
      self.Close()
  
  def OnEditar( self, event ):
    event.Skip()

  def OnMover( self, event ):
    event.Skip()

  def OnCrearEtiquetaIzq( self, event ):
    '''Se crea etiqueta izquierda.'''
    self.__crear_caja(self.m_panel_izqScroll)
    
  def OnborrarEtiquetaIzq( self, event ):
    objeto = self.ultimo_objeto
    if isinstance(objeto, wx.TextCtrl):
      self.__eliminar_etiqueta(objeto)

  def OnCrearEtiquetaCentral( self, event ):
    '''Se crea etiqueta central.'''
    self.__crear_caja(self.m_panel_centralScroll)

  def OnborrarEtiquetaCentral( self, event ):
    objeto = self.ultimo_objeto
    if isinstance(objeto, wx.TextCtrl):
      self.__eliminar_etiqueta(objeto)

  def OnborrarEtiquetaDer( self, event ):
    objeto = self.ultimo_objeto
    if isinstance(objeto, wx.TextCtrl):
      self.__eliminar_etiqueta(objeto)

  def OnCrearEtiquetaDer( self, event ):
    '''Se crea etiqueta derecha.'''
    self.__crear_caja(self.m_panel_derScroll)

  def OnCargarTablero( self, event ):
    self.__cargar_datos_json()

  def OnSalvarTablero( self, event ):
    self.__salvar_datos_json()

  def OnAyuda( self, event ):
    event.Skip()
  
  # ##################
  # Métodos auxiliares
  # ##################
  
  def __activar_botones(self, opcion = True):
    
    for i in [self.m_bpButton_AcercaDe, self.m_bpButton_Ayuda, self.m_bpButton_BorrarEtiquetaCentral, \
               self.m_bpButton_BorrarEtiquetaDer, self.m_bpButton_BorrarEtiquetaIzq, \
               self.m_bpButton_CrearEtiquetaCentral, self.m_bpButton_CrearEtiquetaDer, self.m_bpButton_CrearEtiquetaIzq, \
               self.m_bpButton_Salvar, self.m_bmToggleBtn_Editar, self.m_bmToggleBtn_Mover]:
      if opcion: i.Enable()
      else: i.Disable()
      
  def __salvar_datos_json(self):
    '''Método para salvar los tres paneles en fichero json'''
    
    # Abrimos el fichero json, si existe.
    if platform.system() == "Windows": sep = "\\"
    if platform.system() == "Linux": sep = "/"
    nfichero = "recursos{}/organizador.json".format(sep)
    
    if not f_exists(nfichero):
      datos = {}
    else:
      f = open(nfichero, "r")
      # Cargamos los datos.
      datos = json.load(f)
      f.close()
      
    # Creamos entrada.
    clave = self.m_textCtrl_Proyecto.GetValue().strip()
    if len(clave) != 0:
      
      # Creamos las 3 listas pendiente, en progreso y terminado.
      l_pend = []
      l_prog = []
      l_term =[]
      
      for i in [(self.m_panel_izqScroll, l_pend), (self.m_panel_centralScroll, l_prog), \
                (self.m_panel_derScroll, l_term)]:
        panel = i[0]
        sizer_panel = panel.boxsizer
        for indice in range(sizer_panel.GetItemCount()):
          item = sizer_panel.GetItem(indice)
          i[1].append(item.GetWindow().GetValue().strip())
        
      datos[clave] = [{'pendiente': l_pend,
                       'en_progreso' : l_prog,
                       'terminado' : l_term}]
    
    #  Abrimos fichero y guardamos el json.
    f = open(nfichero, "w")
    json.dump(datos, f)
    f.close()
 
  def __limpiar_tableros(self):
    
    for i in [self.m_panel_centralScroll, self.m_panel_izqScroll, self.m_panel_derScroll]:
      
      sizer_panel = i.boxsizer
      
      for j in range(sizer_panel.GetItemCount()):
        objeto = sizer_panel.GetItem(0).GetWindow()
        sizer_panel.Detach(0)
        objeto.DestroyLater()    
    
    self.ultimo_objeto = None
    self.origen_objeto = None
    
    self.m_panel_izqScroll.boxsizer.Clear()
    self.m_panel_derScroll.boxsizer.Clear()
    self.m_panel_centralScroll.boxsizer.Clear()
           
    self.m_panel_derScroll.boxsizer.Layout()
    self.m_panel_izqScroll.boxsizer.Layout()            
    self.m_panel_centralScroll.boxsizer.Layout()      
    
  def __cargar_datos_json(self):
    '''Método para cargar los tres paneles en fichero json'''
    
    # Abrimos el fichero json, si existe.
    if platform.system() == "Windows": sep = "\\"
    if platform.system() == "Linux": sep = "/"
    nfichero = "recursos{}/organizador.json".format(sep)
    
    if not f_exists(nfichero):
      wx.MessageBox("No hay proyectos disponibles", "Cargar Proyecto", wx.ICON_EXCLAMATION)
    else:
      # Cargamos los datos.
      f = open(nfichero, "r")
      datos = json.load(f)
      f.close()
      
      # Recuperamos claves y las ordenadomos
      claves = sorted(list(datos.keys()))
      
      popup = Seleccionar(self, "Proyectos disponibles", claves)
      if popup.ShowModal() == wx.ID_OK:
        
        valor_seleccionado = popup.elemento_seleccionado  
        
        # Se recuperan los datos de los tableros.
        elementos = datos[valor_seleccionado]
        
        # Nombre del proyecto.
        self.m_textCtrl_Proyecto.SetValue(valor_seleccionado)
        
        # Se limpian los tableros.
        self.__limpiar_tableros()
        
        # Se cargan los tableros.
        for i in [(self.m_panel_izqScroll, elementos[0]["pendiente"]), 
                  (self.m_panel_centralScroll, elementos[0]["en_progreso"]),
                  (self.m_panel_derScroll, elementos[0]["terminado"])]:
          
          for dato in i[1]:
            self.__crear_caja(i[0], dato)
            
        # Se activan los botones.
        self.__activar_botones()
      
      # Se destruye la ventana modal de selección de proyecto.
      popup.Destroy()      
      
    # Creamos entrada.
    clave = self.m_textCtrl_Proyecto.GetValue().strip()
    if len(clave) != 0:
      
      # Creamos las 3 listas pendiente, en progreso y terminado.
      l_pend = []
      l_prog = []
      l_term =[]
      
      for i in [(self.m_panel_izqScroll, l_pend), (self.m_panel_centralScroll, l_prog), \
                (self.m_panel_derScroll, l_term)]:
        panel = i[0]
        sizer_panel = panel.boxsizer
        for indice in range(sizer_panel.GetItemCount()):
          item = sizer_panel.GetItem(indice)
          i[1].append(item.GetWindow().GetValue().strip())
        
      datos[clave] = [{'pendiente': l_pend,
                       'en_progreso' : l_prog,
                       'terminado' : l_term}]
    
    #  Abrimos fichero y guardamos el json.
    f = open(nfichero, "w")
    json.dump(datos, f)
    f.close()
    
  def __crear_paneles(self, panel):
    '''Método de creación de paneles de la aplicación'''
    # Se crea un sizer vertical para el panel.
    box_i = wx.BoxSizer(wx.VERTICAL) 
    panel.SetSizer(box_i)
    panel.Layout()
    box_i.Fit(panel)
  
    # Creamos panel con scroll dentro del panel.
    panelScroll = PanelConScroll(panel)
    panelScroll.SetBackgroundColour(wx.Colour(255, 255, 255))
    
    # Se añade el panel con scroll dentro del panel.
    box_i.Add(panelScroll, 1, wx.EXPAND|wx.ALL, 5)
    
    # Reajustamos el gráfico.
    panel.Layout()
    panelScroll.SetupScrolling() 
        
    # Manejadores de eventos.
    panelScroll.Bind(wx.EVT_LEFT_UP, self.OnClickPanel)    
    
    # Se devuelve el panel con Scroll
    return panelScroll
  
  def __crear_caja(self, panel, dato = None):
    '''Método que crea una caja (etiqueta) en el panel'''
    control_texto = wx.TextCtrl(panel, wx.ID_ANY, wx.EmptyString, \
                                wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE)
    panel.boxsizer.Add(control_texto, 0, wx.ALL|wx.EXPAND, 5 )

    control_texto.SetBackgroundColour(wx.Colour(18, 138, 61))
    control_texto.SetForegroundColour(wx.Colour(255, 255, 255))

    if dato is not None: control_texto.SetValue(dato)
    
    # Manejadores de eventos para la caja.
    
    control_texto.Bind(wx.EVT_KEY_UP, self.onPulsarTecla)
    control_texto.Bind(wx.EVT_KILL_FOCUS, self.onDejarFoco)
    control_texto.Bind(wx.EVT_SET_FOCUS, self.onObtenerFoco)
    control_texto.Bind(wx.EVT_LEFT_UP, self.onClickIzq)
    control_texto.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
    control_texto.Bind(wx.EVT_CHAR, self.onChar)

    # Actualizamos el layout del sizer.
    panel.boxsizer.Layout()
  
    # Pasamos el foco a la nueva etiqueta.
    control_texto.SetFocus()
    
  def __mover_etiqueta_teclado(self, panel_destino, sizer, indice, objeto):
    '''Mueve las etiquetas según en el panel donde se encuentre'''
    
    objeto.Reparent(panel_destino)
                  
    # Movemos la caja de texto de la izquierda y la llevamos a la derecha.
    if indice >= 0:
      # Eliminamos la caja del sizer de la izquierda
      sizer.Detach(indice)
      # Vemos si podemos colocarla a la misma altura.
      t = panel_destino.boxsizer.GetItemCount()
      if t >= indice:
        panel_destino.boxsizer.Insert(indice, objeto, 0,wx.ALL|wx.EXPAND,5)
      else:
        panel_destino.boxsizer.Insert(t, objeto, 0,wx.ALL|wx.EXPAND,5)    
  
  def __colorear_caja(self, objeto, color_texto, color_fondo, estilo_letra, grueso_letra):
    '''Colorea la caja pasada como parámetro'''
    
    t = objeto.GetValue()
    objeto.Clear()
    objeto.SetForegroundColour(color_texto)
    objeto.SetBackgroundColour(color_fondo)
    objeto.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, \
                           estilo_letra, grueso_letra, False, wx.EmptyString))
    objeto.SetValue(t.strip())
    objeto.Refresh()
    
  def __eliminar_etiqueta(self, objeto):
    '''Se elimina etiqueta'''
    
    info = objeto.GetValue()
    ret = wx.MessageBox("¿Eliminar <<{}>>...?".format(info), "Eliminar", wx.YES_NO | wx.ICON_WARNING)
    if ret == wx.YES:
      # Buscamos el objeto dentro del sizer
      panel = objeto.GetParent()
      sizer_panel = panel.boxsizer
      
      for indice in range(sizer_panel.GetItemCount()):
        item = sizer_panel.GetItem(indice)
        if objeto == item.GetWindow():
          break   
      
      # Eliminamos el objeto del sizer
      if not sizer_panel.IsEmpty():
        sizer_panel.Detach(indice)

      self.ultimo_objeto = None
      objeto.DestroyLater()

      # Actualizamos todo
      self.m_panel_derScroll.boxsizer.Layout()
      self.m_panel_izqScroll.boxsizer.Layout()            
      self.m_panel_centralScroll.boxsizer.Layout() 
  
  # ####################################
  #  Manejadores de eventos de etiquetas
  # ####################################

  def onChar(self, event):
    # Se elimina etiqueta si el botón de editar no está activado y se pulsa la tecla Supr.
    if event.GetKeyCode() == wx.WXK_DELETE and not self.m_bmToggleBtn_Editar.GetValue():
      
      objeto = event.GetEventObject()
      self.__eliminar_etiqueta(objeto)
      
      #info = objeto.GetValue()
      #ret = wx.MessageBox("¿Eliminar <<{}>>...?".format(info), "Eliminar", wx.YES_NO | wx.ICON_WARNING)
      #if ret == wx.YES:
        ## Buscamos el objeto dentro del sizer
        #panel = objeto.GetParent()
        #sizer_panel = panel.boxsizer
        
        #for indice in range(sizer_panel.GetItemCount()):
          #item = sizer_panel.GetItem(indice)
          #if objeto == item.GetWindow():
            #break   
        
        ## Eliminamos el objeto del sizer
        #if not sizer_panel.IsEmpty():
          #sizer_panel.Detach(indice)

        #self.ultimo_objeto = None
        #objeto.DestroyLater()

        ## Actualizamos todo
        #self.m_panel_derScroll.boxsizer.Layout()
        #self.m_panel_izqScroll.boxsizer.Layout()            
        #self.m_panel_centralScroll.boxsizer.Layout()            
        
    # Se puede modificar solo si el botón editar está activado.
    if self.m_bmToggleBtn_Editar.GetValue():
      event.Skip()            

  def OnClickPanel( self, event ):
    if event.ControlDown() and self.ultimo_objeto is not None and self.m_bmToggleBtn_Mover.GetValue():
      # Si la etiqueta está dentro de su mismo panel, no se hace nada.
      panel_actual = event.GetEventObject()
      # Panel de la etiqueta.
      panel_etiqueta = self.ultimo_objeto.GetParent()
      if not panel_actual == panel_etiqueta:
        # Buscamos el número total de elementos del panel de destino,
        # cambiamos el padre e insertamos en la última posición.
        indice = panel_actual.boxsizer.GetItemCount()

        # Buscamos el Id del sizer de la etiqueta.
        sizer = self.ultimo_objeto.GetParent().boxsizer
        for index in range(sizer.GetItemCount()):
          item = sizer.GetItem(index)
          if self.ultimo_objeto == item.GetWindow():
            break                     

        panel_etiqueta.boxsizer.Detach(index)
        self.ultimo_objeto.Reparent(panel_actual)
        panel_actual.boxsizer.Insert(indice, self.ultimo_objeto, 0,wx.ALL|wx.EXPAND,5)    

        panel_actual.boxsizer.Layout()
        panel_etiqueta.boxsizer.Layout()                
        
        # Damos el foco.
        self.ultimo_objeto.SetFocus()
        
    event.Skip()

  def OnKeyDown(self, event):
    if self.m_bmToggleBtn_Mover.GetValue:
      event.GetEventObject().SetFocus() 
      if event.ControlDown():
        self.origen_objeto = event.GetEventObject()
    event.Skip()

  def onClickIzq(self, event):
    if self.m_bmToggleBtn_Mover.GetValue() and event.ControlDown() and self.origen_objeto is not None:
      
      objeto = event.GetEventObject()
      
      if objeto.GetParent() == self.m_panel_izqScroll:
        sizer = self.m_panel_izqScroll.boxsizer
      elif objeto.GetParent() == self.m_panel_derScroll:
        sizer = self.m_panel_derScroll.boxsizer
      elif objeto.GetParent() == self.m_panel_centralScroll:
        sizer = self.m_panel_centralScroll.boxsizer            

      # Buscamos el índice dentro del sizer destino.
      for index_destino in range(sizer.GetItemCount()):
        item = sizer.GetItem(index_destino)
        if objeto == item.GetWindow():
          break            

      # Buscamos el índice dentro del sizer origen.
      sizer_origen = self.origen_objeto.GetParent().boxsizer
      for index_origen in range(sizer_origen.GetItemCount()):
        item = sizer_origen.GetItem(index_origen)
        if self.origen_objeto == item.GetWindow():
          break            

      # Si están en el mismo panel, habrá que borrar el origen e insertarlo delante del destino.
      if objeto.GetParent() == self.origen_objeto.GetParent():
        
        if index_destino != index_origen:
          # Borramos del sizer el elemento origen (el que queremos desplazar).
          sizer.Detach(index_origen)
          
          # Insertamos en la posición del destino. 
          sizer.Insert(index_destino, self.origen_objeto, 0,wx.ALL|wx.EXPAND,5)    

          # self.ultimo_objeto = event.GetEventObject()
          self.origen_objeto.SetFocus()
          self.origen_objeto.Refresh()
      else:
        # El origen y el destino están en paneles distintos. Primero borramos del sizer
        # el elemento origen (el que queremos desplazar).
        sizer_origen.Detach(index_origen)
        
        # Cambiamos el padre.                
        self.origen_objeto.Reparent(objeto.GetParent())
        
        # E insertamos en el sizer del nuevo padre.
        sizer.Insert(index_destino, self.origen_objeto, 0,wx.ALL|wx.EXPAND,5)    
        
        # Damos el foco.
        self.origen_objeto.SetFocus()
        self.origen_objeto.Refresh()                
        
      self.m_panel_derScroll.boxsizer.Layout()
      self.m_panel_izqScroll.boxsizer.Layout()
      self.m_panel_centralScroll.boxsizer.Layout()
      
  def onDejarFoco(self, event):
    '''Código asociado a dejar el foco de la caja'''
    objeto = event.GetEventObject()
    self.__colorear_caja(objeto, wx.Colour(255, 255, 255), wx.Colour(18, 138, 61), wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
    self.ultimo_objeto = objeto

  def onObtenerFoco( self, event ):
    if self.m_bmToggleBtn_Editar.GetValue():
      objeto = event.GetEventObject()
      self.__colorear_caja(objeto, wx.Colour(255, 255, 255), self.color_en_edicion, wx.FONTSTYLE_SLANT, wx.FONTWEIGHT_BOLD)
      
  def onPulsarTecla(self, event):
    
    accion = ""
    
    if event.GetKeyCode() == wx.WXK_UP: accion = "subir"
    if event.GetKeyCode() == wx.WXK_DOWN: accion = "bajar"
    if event.GetKeyCode() == wx.WXK_LEFT: accion = "izquierda"
    if event.GetKeyCode() == wx.WXK_RIGHT: accion = "derecha"
    
    objeto = event.GetEventObject()
    
    if objeto.GetParent() == self.m_panel_izqScroll:
      sizer = self.m_panel_izqScroll.boxsizer
    elif objeto.GetParent() == self.m_panel_derScroll:
      sizer = self.m_panel_derScroll.boxsizer
    elif objeto.GetParent() == self.m_panel_centralScroll:
      sizer = self.m_panel_centralScroll.boxsizer
    
    if accion in ["subir", "bajar", "izquierda", "derecha"]:

      if self.m_bmToggleBtn_Mover.GetValue():
        seguir = False

        # Buscamos el índice dentro del sizer.
        for index in range(sizer.GetItemCount()):
          item = sizer.GetItem(index)
          if item.GetWindow().FindFocus() == item.GetWindow():
            seguir = True
            break

        if accion == "subir":
          if seguir and index > 0:
            sizer.Detach(index)
            index -= 1
            if index >=0: sizer.Insert(index, objeto, 0,wx.ALL|wx.EXPAND,5)

        if accion == "bajar":
          aux = sizer.GetItemCount()
          if seguir and index < sizer.GetItemCount() - 1:
            sizer.Detach(index)
            index += 1
            if index <= aux - 1:
              sizer.Insert(index, objeto, 0,wx.ALL|wx.EXPAND,5)

        if seguir:
            
          # Mover la etiqueta desde el panel izquierdo al panel central.
          if accion == "derecha" and objeto.GetParent() == self.m_panel_izqScroll:
            self.__mover_etiqueta_teclado(self.m_panel_centralScroll, sizer, index, objeto)
          elif accion == "izquierda" and objeto.GetParent() == self.m_panel_derScroll:
            # Mover la etiqueta desde el panel derecho al panel central.
            self.__mover_etiqueta_teclado(self.m_panel_centralScroll, sizer, index, objeto)
          elif accion == "derecha" and objeto.GetParent() == self.m_panel_centralScroll:
            # Mover la etiqueta desde el panel central al panel derecho.
            self.__mover_etiqueta_teclado(self.m_panel_derScroll, sizer, index, objeto)
          elif accion == "izquierda" and objeto.GetParent() == self.m_panel_centralScroll:
            # Mover la etiqueta desde el panel central al panel izquierdo.
            self.__mover_etiqueta_teclado(self.m_panel_izqScroll, sizer, index, objeto)

      self.m_panel_derScroll.boxsizer.Layout()
      self.m_panel_izqScroll.boxsizer.Layout()
      self.m_panel_centralScroll.boxsizer.Layout()
    
      objeto.SetFocus()
            
app = wx.App()

# Definimos el idioma al castellano de todos los componentes.
locale = wx.Locale(wx.LANGUAGE_SPANISH)

ventana = Ventana(None)
ventana.Show()
app.MainLoop()