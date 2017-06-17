#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime
import sys

# =====================================================================
class Logger( object ):

    # -------------------------------------------------------------
    def __init__(self, path):

        self.path = path;

    # -------------------------------------------------------------
    def trace( self):

        exc_type, exc_obj, tb = sys.exc_info()
        f = tb.tb_frame            

        self._LOG( 'E', ' FILE   : ['+f.f_code.co_filename+']' );
        self._LOG( 'E', ' METHOD : ['+str(tb.tb_frame.f_code)+']' );
        self._LOG( 'E', ' ERROR  : ['+str(exc_type)+'] >>> ['+str(exc_obj)+'] LINE: ['+str(tb.tb_lineno)+']' );
 
    # -------------------------------------------------------------
    def I( self, data):
        self._LOG( 'I', str(data) );

    # -------------------------------------------------------------
    def W( self, data):
        self._LOG( 'W', str(data) );

    # -------------------------------------------------------------
    def E( self, data):
        self._LOG( 'E', str(data) );
        self.trace();

    # -------------------------------------------------------------
    def F( self, data):
        self._LOG( 'F', str(data) );
        self.trace();

    # -------------------------------------------------------------
    def _LOG( self, type_t, data ):

        with open( self.path+'/'+'_'+type_t+'_'+self.DATE()+'.log', "a+" ) as FSW:
            FSW.write( '['+type_t+']:['+self.DATETIME()+'] '+str( data )+"\n" );

    # -------------------------------------------------------------
    def STAMP( self, mk_int=False ):

        if( mk_int ):
            return int( datetime.now().strftime('%s') ); # '1491102083'
        return datetime.now().strftime('%s');

    def DATETIME( self ):
        return datetime.now().strftime('%d-%m-%Y %H:%m:%S'); # '02-04-2017 03:04:16'

    def DATE( self ):
        return datetime.now().strftime('%d-%m-%Y'); # '02-04-2017'

# =====================================================================
if __name__ == '__main__':

    Logger = Logger();

