module Greenwich
  #===========================================================================
  # Class for Rotation given the Fukushima-Williams angles
  #===========================================================================
  class RotationFw
    #-------------------------------------------------------------------------
    # Form rotation matrix given the Fukushima-Williams angles.
    #
    # @param:  gam_b
    # @param:  phi_b
    # @param:  psi
    # @param:  eps
    # @return: r  (Rotation matrix)
    #-------------------------------------------------------------------------
    def fw2m(gam_b, phi_b, psi, eps)
      r = init_r
      r = rotate_z(r, gam_b)
      r = rotate_x(r, phi_b)
      r = rotate_z(r, -1 * psi)
      r = rotate_x(r, -1 * eps)
      return r
    rescue => e
      raise
    end
  end
end

