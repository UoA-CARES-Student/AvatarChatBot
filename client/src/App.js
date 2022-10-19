import './App.css';
import {
  Routes,
  Route,
  Link
} from "react-router-dom";
import * as React from 'react';
import PropTypes from 'prop-types';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Divider from '@mui/material/Divider';
import Drawer from '@mui/material/Drawer';
import IconButton from '@mui/material/IconButton';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemText from '@mui/material/ListItemText';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import Home from './pages/Home/Home';
import Vid2Vid from './pages/Vid2Vid/Vid2Vid';
import Img2Vid from './pages/Img2Vid/Img2Vid';

const drawerWidth = 240;
const navItems = ['Img2Img', 'Vid2Vid'];

function App(props) {
  const { window } = props;
  const [mobileOpen, setMobileOpen] = React.useState(false);

  const handleDrawerToggle = () => {
    setMobileOpen(!mobileOpen);
  };

  const drawer = (
    <Box onClick={handleDrawerToggle} sx={{ textAlign: 'center' }}>
      <Typography variant="h6" sx={{ my: 2 }}>
        MUI
      </Typography>
      <Divider />
      <List>
        {navItems.map((item) => (
          <ListItem key={item} disablePadding>
            <ListItemButton sx={{ textAlign: 'center' }}>
              <ListItemText primary={item} />
            </ListItemButton>
          </ListItem>
        ))}
      </List>
    </Box>
  );

  const container = window !== undefined ? () => window().document.body : undefined;

  return (
    <Box sx={{ display: 'flex' }}>
      <AppBar component="nav">
        <Toolbar>
          <IconButton
            color="inherit"
            aria-label="open drawer"
            edge="start"
            onClick={handleDrawerToggle}
            sx={{ mr: 2, display: { sm: 'none' } }}
          >
          </IconButton>
          
          <Button key="img2vid" sx={{ flexGrow: 1, display: { xs: 'none', sm: 'block' } }} component={Link} to="/">
            <Typography
              variant="h6"
              component="div"
              sx={{ color: '#fff' }}
            >
            Avatar Chatbot
            </Typography>
          </Button>
          
          <Box sx={{ display: { xs: 'none', sm: 'block' } } }>
            <Button key="img2vid" sx={{ color: '#fff' }} component={Link} to="img2vid">
              Img2Vid
            </Button>

            <Button key="vid2vid" sx={{ color: '#fff' }} component={Link} to="vid2vid">
              Vid2Vid
            </Button>

    
          </Box>
        </Toolbar>
      </AppBar>

      
      <Box component="nav">
        <Drawer
          container={container}
          variant="temporary"
          open={mobileOpen}
          onClose={handleDrawerToggle}
          ModalProps={{
            keepMounted: true, // Better open performance on mobile.
          }}
          sx={{
            display: { xs: 'block', sm: 'none' },
            '& .MuiDrawer-paper': { boxSizing: 'border-box', width: drawerWidth },
          }}
        >
          {drawer}
        </Drawer>
      </Box>
      <Box component="main" sx={{ p: 3 }}>
        <Toolbar />
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="vid2vid" element={<Vid2Vid />} />
            <Route path="img2vid" element={<Img2Vid />} />
          </Routes>
      </Box>
    </Box>
  );
}

App.propTypes = {
  window: PropTypes.func,
};

export default App;

