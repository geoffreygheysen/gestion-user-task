class DbTools:
    def __init__(self, session):
        self.session = session
    
    def commit(self):
        try:
            self.commit()
        except Exception as e:
            self.session.rollback()
            raise e
        finally:
            self.session.close()